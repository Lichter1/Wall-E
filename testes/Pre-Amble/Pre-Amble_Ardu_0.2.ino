String command;

// Define Motor Outputs on PCA9685 board
int motorX = 0;

// Include Wire Library for I2C Communications
#include <Wire.h>
 
// Include Adafruit PWM Library
#include <Adafruit_PWMServoDriver.h>
 
#define MIN_PULSE_WIDTH       650
#define MAX_PULSE_WIDTH       2350
#define FREQUENCY             50
 
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x7F);



void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.println("Start"); 
 pwm.begin();
 pwm.setPWMFreq(FREQUENCY);
}


void moveServo(int controlIn, int motorOut)
{
    
   if (controlIn > 1){
    controlIn = 1;
   }
   
   else if (controlIn < -1){
    controlIn = -1;
   }
  int pulse_wide, pulse_width ;
  

  // Convert to pulse width
  pulse_wide = map(controlIn, -1, 1, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  
  //Control Motor
  pwm.setPWM(motorOut, 0, pulse_width);
}
  
  

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    command = Serial.readIntUntil('\n');
    //command.trim();
    command = "Raspbeery pi Command: " + command;
    Serial.println(command);
    
    moveServo(command, motorX);
    
    Serial.println("Start");  
  }}
