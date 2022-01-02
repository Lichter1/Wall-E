String command;
String RaspiCommand;
// Define Motor Outputs on PCA9685 board
int motorX = 0;

// Include Wire Library for I2C Communications
#include <Wire.h>
 
// Include Adafruit PWM Library
#include <Adafruit_PWMServoDriver.h>
 
#define MIN_PULSE_WIDTH       1000
#define MAX_PULSE_WIDTH       2000
#define FREQUENCY             50
 
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x7F);



void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.setTimeout(50);
Serial.println("Start"); 
 pwm.begin();
 pwm.setPWMFreq(FREQUENCY);
}


void moveServo(int controlIn, int motorOut)
{
    
   if (controlIn > 100){
    controlIn = 100;
   }
   
   else if (controlIn < -100){
    controlIn = -100;
   }
  int pulse_wide, pulse_width ;
  //Serial.println(controlIn);

  // Convert to pulse width
  pulse_wide = map(controlIn, -100, 100, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  RaspiCommand = "Raspbeery pi Command: " + String(pulse_wide);
  Serial.println(RaspiCommand);
  //Control Motor
  pwm.setPWM(motorOut, 0, pulse_width);
  //delay(1000);
}
  
  

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();
    RaspiCommand = "Raspbeery pi Command: " + command;
    //Serial.println(RaspiCommand);
    
    moveServo( (command.toFloat()*100), motorX);
    
    Serial.println("Start");  
  }}
