import serial
ser = serial.Serial('COM7', 9800, timeout=1)

while(True):
    sen = ser.readline()
    print(sen)