/*  Arduino DC Motor Control - PWM | H-Bridge | L298N

*/
#define enA 11
#define in1 10
#define in2 9
#define enB 6
#define in3 8
#define in4 7
int SEspeed = 0;
String command;
int SEturn = 0;
int x = 0;
int SEhead_x = 90;


// Define Motor Outputs on PCA9685 board
int motorA = 0;
int motorB = 4;
int motorC = 8;

// Include Wire Library for I2C Communications
#include <Wire.h>
 
// Include Adafruit PWM Library
#include <Adafruit_PWMServoDriver.h>
 
#define MIN_PULSE_WIDTH       650
#define MAX_PULSE_WIDTH       2350
#define FREQUENCY             50
 
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();


/////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);
}



/////////////////////////////////////////////////////////////////////////////////////////////

void moveMotor(int Speed, int Turn){
  
   int leftSpeed = Speed - Turn;
   int rightSpeed = Speed + Turn;
   
   if (leftSpeed > 255){
    leftSpeed = 255;
   }
   
   else if (leftSpeed < -255){
    leftSpeed = -255;
   }
   
   else if (abs(leftSpeed) < 70) {
    leftSpeed = 0;
   }
   
   if (rightSpeed > 255){
         rightSpeed = 255;
   }
   
   else if (rightSpeed<=-255){
    rightSpeed = -255;
   }
   
   else if (abs(rightSpeed) < 70) {
    rightSpeed = 0;
   }

//////////////////////////////////////////////////////
  
   if (leftSpeed > 0){
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
   }
   
    else {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    }

  if (rightSpeed > 0){
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
   }
   
    else {
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    }


 
  analogWrite(enA, abs(rightSpeed)); // Send PWM signal to motor A
  analogWrite(enB, abs(leftSpeed)); // Send PWM signal to motor B
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void moveServo(int controlIn, int motorOut)
{
    
   if (controlIn > 180){
    controlIn = 180;
   }
   
   else if (controlIn < 0){
    controlIn = 0;
   }
  int pulse_wide, pulse_width ;
  

  // Convert to pulse width
  pulse_wide = map(controlIn, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  
  //Control Motor
  pwm.setPWM(motorOut, 0, pulse_width);
}


////////////////////////////////////////////////////////////////////////////////////////

      
void loop() {
 
 if (Serial.available() == 0 && x > 0){
      delay(1500);
      SEspeed = 0;
      SEturn = 0;
      SEhead_x = 90;
      x = 0;
    }

  
  while (Serial.available() > 0){
     delay(100);
     //int Head = Serial.parseInt();
     SEspeed = Serial.parseInt();
     SEturn = Serial.parseInt();
     SEhead_x = Serial.parseInt();
     x = 1;
     if (Serial.available()) {
      command = Serial.readStringUntil('\n');
     
      }}
  
   moveMotor(SEspeed, SEturn);
   moveServo(SEhead_x, motorA);
}
