#include <Servo.h> 

const int servoPin1 = 2;
const int servoPin2 = 3;
const int servoPin3 = 4;
const int servoPin4 = 5;
const int servoPin5 = 6;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

int angle1 = 0;
int angle2 = 180;
int angle3 = 180;
int angle4 = 0;
int angle5 = 0;

void setup() {
  Serial.begin(9600);
  servo1.attach(servoPin1);
  servo2.attach(servoPin2); 
  servo3.attach(servoPin3);
  servo4.attach(servoPin4); 
  servo5.attach(servoPin5);

  servo1.write(0); 
  servo2.write(180); 
  servo3.write(180); 
  servo4.write(0);
  servo5.write(0);

  delay(3000);
}

int i;
int j;
int k;

//angle1 = 0~90
//angle2 = 90~180
//angle3 = 90~180
//angle4 = 0~90

void loop() {
  for(i = 0; i < 45; i++) {
    servo1.write(i);
    servo2.write(180 - i);
    delay(15);
  }
  
  for(j = 0; j < 135; j++) {
    servo3.write(180 - j);
    servo4.write(j);
    delay(15);
  }

  for(k = 0; k < 180; k++) {
    servo5.write(k);
    delay(15);
  }

  delay(3000);
///////////////////////////////////stop/////////////////

  for(k = 180; k > 0; k--) {
    servo5.write(k);
    delay(15);
  }

  for(j = 135; j > 60; j--) {
    servo3.write(180 - j);
    servo4.write(j);
    delay(15);
  }

  for(i = 45; i < 70; i++) {
    servo1.write(i);
    servo2.write(180 - i);
    delay(15);
  }

  delay(2000);
  ///////////////////////////stop2////////////////////


  for(j = 70; j > 0; j--) {
    servo3.write(180 - j);
    servo4.write(j);
    delay(15);
  }
  
  for(i = 80; i > 0; i--) {
    servo1.write(i);
    servo2.write(180 - i);
    delay(15);
  }
  
    delay(3000);
} 
