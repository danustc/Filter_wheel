#include <Servo.h>
/*
 * Please use the digital ports, 3,5,6,9 on the Arduino.
 */
Servo serv_405, serv_488, serv_561, serv_640;
int pos = 90;
int which_servo = 1;
int delay_time = 300;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  serv_405.attach(3);
  serv_488.attach(5);
  serv_561.attach(6);
  serv_640.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
   while(Serial.available()==0){};
   if(Serial.available()==2){
     which_servo = Serial.read();
     pos = Serial.read();
   
    if(which_servo == 1){
      serv_405.write(pos);
    }//endif
    else if (which_servo ==2){
      serv_488.write(pos);
    }
    else if (which_servo ==3){
      serv_561.write(pos);
    }
    else if (which_servo ==4){
      serv_640.write(pos);
    }
    Serial.flush();
    delay(delay_time);
   }//endif
}
