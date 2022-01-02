
// Define motor pins
#define enA 11
#define in1 10
#define in2 9
#define enB 6
#define in3 8
#define in4 7

// Define veribols
String command;
String RaspiCommand;

// SErial input
int SEspeed = 0;
int SEturn = 0;
int SEhead_X = 0;
int SEhead_Y_H = 0;
int SEhead_Y_L = 0;
int SEhead_I_R = 0;
int SEhead_I_L = 0;
int SEhead_A_R = 0;
int SEhead_A_L = 0;

// Define Motor Outputs on PCA9685 board
int motorX = 0;
int motorY_H = 1;
int motorY_L = 2;
int motorI_R = 3;
int motorI_L = 4;
int motorA_R = 5;
int motorA_L = 6;

// Include Wire Library for I2C Communications
#include <Wire.h>
 
// Include Adafruit PWM Library
#include <Adafruit_PWMServoDriver.h>
 
#define MIN_PULSE_WIDTH       1000
#define MAX_PULSE_WIDTH       2000
#define FREQUENCY             50
 
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x7F);



void setup() {
//Serial set up
Serial.begin(9600);
Serial.setTimeout(50);

//PCA set up
pwm.begin();
pwm.setPWMFreq(FREQUENCY);

// Pins set up
pinMode(enA, OUTPUT);
pinMode(enB, OUTPUT);
pinMode(in1, OUTPUT);
pinMode(in2, OUTPUT);
pinMode(in3, OUTPUT);
pinMode(in4, OUTPUT);

// Arduino ready to start
Serial.println("Start"); 
}



////////////////////////////////////////////////////////////////////////
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

/////////////////////////////////////////////////////////////////////////////////////




void moveServo(int controlIn, int motorOut)
{
    
   if (controlIn > 180){
    controlIn = 180;
   }
   
   else if (controlIn < 0){
    controlIn = 0;
   }
  int pulse_wide, pulse_width ;
  //Serial.println(controlIn);

  // Convert to pulse width
  pulse_wide = map(controlIn, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  RaspiCommand = "Raspbeery pi Command: " + String(pulse_wide);
  Serial.println(RaspiCommand);
  //Control Motor
  pwm.setPWM(motorOut, 0, pulse_width);
  //delay(1000);
}
  
  //////////////////////////////////////////////////////////////////

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    
    SEspeed = Serial.parseInt();
    SEturn = Serial.parseInt();
    SEhead_X = Serial.parseInt();
    SEhead_Y_H = Serial.parseInt();
    SEhead_Y_L = Serial.parseInt();
    SEhead_I_R = Serial.parseInt();
    SEhead_I_L = Serial.parseInt();
    SEhead_A_R = Serial.parseInt();
    SEhead_A_L = Serial.parseInt();
    
    if (Serial.available()) {
      command = Serial.readStringUntil('\n');
      command.trim();
      RaspiCommand = "Raspbeery pi Command: " + command;
      Serial.println(RaspiCommand);}
    
    
    
   moveMotor(SEspeed, SEturn);
   moveServo(SEhead_X, motorX);
   moveServo(SEhead_Y_H, motorY_H);
   moveServo(SEhead_Y_L, motorY_L);
   moveServo(SEhead_I_R, motorI_R);
   moveServo(SEhead_I_L, motorI_L);
   moveServo(SEhead_A_R, motorA_R);
   moveServo(SEhead_A_L, motorA_L);
    
    Serial.println("Start");  
  }}
