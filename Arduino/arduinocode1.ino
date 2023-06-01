#include"DHT.h"


int a[10];
int ldr=A0 ;
int ledpin= 9;
int ldr_flag=0;
int pump_flag = 0;
int pump = 8;
int i=0;

float h;
float t;


int threshold= 30;
#define DHTPIN 2

#define DHTTYPE DHT11

int dark;
DHT dht(DHTPIN, DHTTYPE);


void setup() {
  
  pinMode(ledpin, OUTPUT);
  Serial.begin(9600);
  dht.begin();
  // put your setup code here, to run once:
  //humidity();
  //Pump();
}

/*void Pump() {
  if(h<threshold) {
    for(i;i<255;i++){
      analogWrite(pump, i);
      delay(30);
    }pump_flag=1;
    

  }else{
    for(i=255;i=0;i--){
      analogWrite(pump, i);
      delay(20);
    }
    //digitalWrite(pump, LOW);
    pump_flag =0;

  }
}*/

/*void humidity() {
  while(true) {
    float h = dht.readHumidity();
    //Serial.println(h);
    delay(1000);

    float t = dht.readTemperature();
    delay(1000);
    return;
  }

  
}*/

void ldr_sensor() {
  int reading = analogRead(ldr);
  int dark = reading/4;
  
    analogWrite(ledpin, dark);
  
  
  //Serial.println(dark);
  
}

void serialcom() {
  Serial.println(h);
  delay(100);
  Serial.println(t);
  delay(100);
  Serial.println(ldr_flag);
  delay(1000);
  Serial.println(pump_flag);
  delay(1000);

}
void loop() {
  float h = dht.readHumidity();
    // Serial.println(h);
    delay(1000);

    float t = dht.readTemperature();
    // Serial.println(t);
    delay(1000);
    
    if(h<threshold) {
      for(i;i<255;i++){
        analogWrite(pump, i);
        delay(30);
      }
    pump_flag=1;
    }else {
      for(i=255;i=0;i--){
      analogWrite(pump, i);
      delay(20);
    }
    //digitalWrite(pump, LOW);
    pump_flag =0;

  }
   // float a[4]={t,h,(dark/255)*100,pump_flag};

  Serial.println((String)"temp="+t+",humidity="+h+",led_intensity="+(dark/255)*100);
  /*
  Serial.println((String)"temp="+t);
  Serial.println((String)"humidity="+h);
  Serial.println((String)"intensity="+(dark/255)*100);
  // Serial.println((String)"pump="+pump_flag);
  */
  delay(1000);
  /*Serial.println(ldr_flag);
  delay(1000);
  Serial.println(pump_flag);
  delay(1000);
  //Serial.println("================================================");
  delay(1000);
  //humidity();
  //Pump();
  //serialcom();
  //ldr_sensor();*/
  
  
  

}
