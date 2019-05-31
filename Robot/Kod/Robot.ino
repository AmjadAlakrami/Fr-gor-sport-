#include <Servo.h>
#include <Wire.h>      // inkluderar olika biblotek 
#include <VL53L0X.h>
#include "EspMQTTClient.h"
#define Pwm_b 5
#define Dir_b1 0  // definerar vilka pins vi ska använda 
#define Dir_b2 4
int dis1= 0; 
int dis2 = 0;
int dis3= 0;      //int variablar
int dis4 = 0;          
int dis5 = 0;       
int dis6 = 0;   
int average = 0;         
bool ON= HIGH; 
bool On_2 = LOW;      //Boolean variablar, kan defineras som HIGH eller LOW, true eller fals 
typedef enum Drivingstates {  //definerar en egen data typ 
  checkdist,                                
  kv,                           //Olika tillstånd 
  kh,                          
  look
};
Drivingstates Drs;

void onConnectionEstablished();

EspMQTTClient client(
 "ABBIndgymIoT_2.4GHz",           // Wifi ssid
  "ValkommenHit!",           // Wifi password
  "192.168.0.119",  // MQTT broker ip
  1883,             // MQTT broker port
  "Amjad",            // MQTT username
  "Ak",       // MQTT password                            array för att connecta till wifi och mqtt broker 
  "microdator",          // Client name
  onConnectionEstablished, // Connection established callback
  true,             // Enable web updater
  true              // Enable debug messages
);

Servo myservo;   //definerar servo som myservo 
VL53L0X sensor;   // definerar VL sensor som sensor 

void setup() {
Serial.begin(9600);  //startar en serie kommunikation
pinMode(Dir_b1, OUTPUT);
pinMode(Dir_b2, OUTPUT);  // definnerar de pins som outputs 
pinMode(Pwm_b, OUTPUT);
myservo.attach(2);   // servo är kopplad till pin 2 "D4 för esp"
myservo.write(96);  //sätter servo på 96 grader 
Wire.begin(12,13);  // vilka pins vi använder för sensor (SDA, SCL)
sensor.init(); //sätter sensor på  
sensor.setTimeout(500); //sätter maximi tiden för hur ofta vi ska få in värden från sensor. i vanliga fall så är det 1000 milisekunder
sensor.startContinuous(); // så att vi får värden hela tiden, inte bara en gång 
pinMode (A0, INPUT);  // definerar analog in variabel .. vi mäter värden vi får ut från motor 
}
int sens() {
  return sensor.readRangeContinuousMillimeters();  // hämta sensor värden i millimeter 
  Serial.println(sens());
 } 
void kor(int vinkel, int hast, bool ON, bool On_2) {  //skapar en void function, sätter int vinkel, int hast, bool ON, bool On_2 som olika argument för den functionen
  sens();
  for (int i=0; i < 1000; i++) {  //for loop 
    average = average + analogRead(A0);// lägger 1000 mätningar från analog in med varandra, o sätter i variabel average som vi definerade förut som int
  }
 average = average/1000; //delar average med 1000, då får vi medle värden. 
 Serial.println(average);
  myservo.write(vinkel);  // värdet på servo = argumenten vinkel 
  digitalWrite(Dir_b2, ON); // värdet på pin Dir_b2 alltså 4 = boolean agumentet ON
  digitalWrite(Dir_b1, On_2);
  analogWrite(Pwm_b, hast); 

  }
 
void onConnectionEstablished(){}

void loop() {  
  switch(Drs){  
    case checkdist: // definerar case checkdist  .. det caseet kör för att roboten kör fram så länge värdet på sensor inte är mindre än 55 och värdet från motor inte är mindre än 365
     if (average < 365) { // om averag, alltså värdet från motor är mindre än 365 
     kor(96, 700, ON, On_2); // kör funktionen kor, sätter värdet på servo 96, värdet på pwm 700, värdet på Dir_b2 HIGH, värdet på Dir_b1 LOW .. bilen kör bakåt 
      client.publish("mess", "kör fram"); // skickar till mqtt broker 
     }
     else { //annars 
      kor(96, 700, !ON, !On_2); // kör funktionen med olika värden på de argumenten .. bilen kör fram 
       client.publish("mess", "kör bak");
      delay(500);
      Drs = look; // bytt caset
     }
     if (sens() < 70){ // om värdet på sensor är mindre än 70
      kor(96, 700, !ON, !On_2);
       client.publish("mess", "kör bak");
      delay(500);
      Drs = look;
     }
     break;  // bryter caset 
    
    case look: // det caset gör att roboten jämför avståndet höger om roboten och vänster om roboten, sen gör att roboten tar vägen där värdet på sensor är högst
     kor(0, 0, !ON, !On_2);
      client.publish("mess", "kollar höger");
     delay(750);
     dis1 = sens(); // sätter värdet från sensor  i en variabel 
     kor(45, 0, !ON, On_2);
     client.publish("mess", "kollar höger");
     delay(750);
     dis2 = sens(); 
        // dis1 och dis2 är värden på sensor från höger sidan, den ena är från 90 grader och den andra från 45 grader
     kor(150, 0, !ON, On_2);
     client.publish("mess", "kollar vänster");
     delay(750);
     dis3= sens();
     kor(180, 0, !ON, On_2);
     client.publish("mess", "kollar vänster");
     delay(750);
     dis4= sens();
     //samma sak för dis3 och dis4 fast för vänster sidan 
     dis5 = (dis1 + dis2)/2;  // adderar sensor värden  från höger sidan, dela de med två, sätta de i en ny variabel
     delay(50);
     dis6 = (dis3 + dis4)/2; 
     delay(50);
     if (dis5 > dis6  ){ // om dis5 är mindre än dis6 
      if (dis5>100){ // och om dis5 är större än 100  
      Drs = kh; //bytt caset
      }
      else { //annars 
       kor(96, 700, !ON, !On_2); //kör bakåt
       client.publish("mess", "kör bak");
       delay(500); 
       Drs = look;     //och bytt caset
       }
      }
     else if (dis6 > dis5 ) { //annars om dis6 mindre än dis5
      if (dis6>100) { //och dis6 mindre än 100
        Drs = kv; // bytt caset 
       }
      else {
        kor(96, 700, !ON, !On_2);
        client.publish("mess", "kör bak");
        delay(500);       
        Drs = look;
       }
     }
      else{
        kor(96, 700, !ON, !On_2);
        client.publish("mess", "kör bak");
        delay(500);
        Drs = look;
      }
     break; 
    
     case kh : // det caset säget åt roboten att kör högeråt 
     kor(45, 0, !ON, On_2);//svänger höger utan att köra 
     delay(500);
     if (sens() > 70){ //om värdet på sensor efter svänger är mer än 70, kör högeråt, o sen byt caset 
      kor(45, 900, ON, On_2);
      client.publish("mess", "svänger höger");
      delay(700);
      kor(96, 0, !ON, On_2);
      client.publish("mess", "kör fram");
      delay(750);
      Drs = checkdist;
     }
     else { // annars så backar den, och byter caset 
      kor(96, 700, !ON, !On_2);
      client.publish("mess", "kör bak");
      delay(500);
      Drs = look;
     }
    break; 

    case kv: // det caset säget åt roboten att kör vänsteråt 
      kor(150, 0, !ON, On_2); //svänger vänster utan att köra 
      delay(500);
      if (sens() > 70){  // om värdet på sensor efter svängen är större än 55, kör vänsteråt, o sen byt caset 
        kor(150, 900, ON, On_2); 
        client.publish("mess", "svänger höger");
        delay(700);
        kor(96, 0, !ON, On_2);
        client.publish("mess", "kör fram");
        delay(750);
        Drs = checkdist;
      }
     else { // annars så backar den, och byter caset 
      kor(96, 700, !ON,!On_2);
      client.publish("mess", "kör bak");
      delay(500);
      Drs = look;
     }
    break; 
  }
  client.loop(); // kör client loopen. 
}


    
