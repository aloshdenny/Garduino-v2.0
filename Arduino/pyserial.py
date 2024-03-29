import serial
import requests
from urllib.request import urlopen
import json

ser = serial.Serial("COM6", 9600)
url = "https://f46a-49-37-226-92.in.ngrok.io/home/api" #Enter required url

while True:
    bin_data = ser.readline()
    bad_data = bin_data.decode()

    # Getting previous API data 
    response = urlopen(url)
    data_json = json.loads(response.read())[0]
    
    # Delete data which is not required
    delete_list = ["temp", "humidity", "led_intensity", "next_spray"] # Check about fertilizer
    for i in delete_list:
        del data_json[i]
    
    bad_datastring = str(data_json)[:-1] + ","
    datastring = ""
    
    # Replacing ' with "
    for i in range(len(bad_datastring)):
        if bad_datastring[i] == "'":
            datastring += '"'
        else:
            datastring += bad_datastring[i]

    # Cleaning data
    # datastring = '{"name": "Tulip","next_spray": "01:02:03","fertilizer_level": 50,"led_intensity": 90,"time_to_sundown": "19:00:00","status": "H",'
    a = bad_data.split(',')
    for i in a[:-1]:
        l = i.split("=")
        try:
            datastring += f'"{l[0]}": {float(l[1])},'
        except ValueError:
            string = l[1].strip();
            if string == "NAN":
                datastring += f'"{l[0]}": 0.0,'
            else:
                datastring += f'"{l[0]}": "{string}",'
        
    l = a[-1].split("=")
    try: 
        datastring +=  f'"{l[0]}": {float(l[1])}' + '}'
    except ValueError:
        string = l[1].strip()
        if string == "NAN":
            datastring +=  f'"{l[0]}": 0.0' + '}'
        datastring +=  f'"{l[0]}": "{string}"' + '}'



    # datastring = '{"name": "Tulip","temp": 0,"humidity": 40,"next_spray": "01:02:03","fertilizer_level": 50,"led_intensity": 90,"time_to_sundown": "19:00:00","status": "H"}'
    # print(data)
    json_object = json.dumps(datastring, indent=4)
    print("Dumped value:\n" + json_object)
    r = requests.put('http://127.0.0.1:8000/home/api/1/', data=datastring)

    print(r)