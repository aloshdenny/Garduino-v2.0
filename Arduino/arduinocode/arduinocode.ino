#include"DHT.h"


int a[10];
int ldr=A0 ;
int ledpin= 9;
int ldr_flag=0;
int pump_flag = 0;
int pump = 13;
int i=0;

float h;
float t;


int threshold= 30;
#define DHTPIN 2

#define DHTTYPE DHT11

int dark;
DHT dht(DHTPIN, DHTTYPE);


void setup() {

  pinMode(pump, OUTPUT);
  pinMode(ledpin, OUTPUT);
  Serial.begin(9600);
  dht.begin();
  //ldr_sensor();
}


/*void ldr_sensor() {
  while(true){
    int reading = analogRead(ldr);
  int dark = reading/4;
  
    analogWrite(ledpin, dark);
  
  //Serial.println(dark);
  }*/
  
  
  
  





void loop() {
  float h = dht.readHumidity();
    // Serial.println(h);
    delay(1000);

    float t = dht.readTemperature();
    // Serial.println(t);
    delay(1000);
    
    if(h<threshold) {
      digitalWrite(pump, HIGH);
      pump_flag=1;
    }
    else {
      digitalWrite(pump, LOW);
      pump_flag=0;
    }
    //ldr_sensor();

    int reading = analogRead(ldr);
  float dark = reading/4;
  float led_intensity = (dark/255)*100;
    analogWrite(ledpin, dark);
    
   // float a[4]={t,h,(dark/255)*100,pump_flag};

 Serial.println((String)"temp="+t+",humidity="+h+",led_intensity="+led_intensity+",next_spray="+pump_flag);
  /*
  Serial.println((String)"temp="+t);
  Serial.println((String)"humidity="+h);
  Serial.println((String)"intensity="+(dark/255)*100);
  // Serial.println((String)"pump="+pump_flag);
  */
  delay(1000);
  
  
  
  
  

}
