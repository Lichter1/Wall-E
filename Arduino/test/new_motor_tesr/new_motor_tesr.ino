/*  Arduino DC Motor Control - PWM | H-Bridge | L298N
         Example 02 - Arduino Robot Car Control
    by Dejan Nedelkovski, www.HowToMechatronics.com
*/
#define enA 11
#define in1 10
#define in2 9
#define enB 6
#define in3 8
#define in4 7
int Speed = 0;
String command;
int turn = 0;
int x = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}


      
void loop() {
  int xAxis = analogRead(A0); // Read Joysticks X-axis
  int yAxis = analogRead(A1); // Read Joysticks Y-axis
  // Y-axis used for forward and backward contro
 if (Serial.available() == 0 && x > 0){
      delay(1500);
      Speed = 0;
      turn = 0;
      x = 0;
    }

  
  while (Serial.available() > 0){

     //int Head = Serial.parseInt();
     Speed = Serial.parseInt();
     turn = Serial.parseInt();
     x = 1;
     if (Serial.available()) {
      command = Serial.readStringUntil('\n');
      command.trim();
     
      }}
    
  
  /*Speed = map(yAxis, 0, 1023, -255, 255);
  int turn = map(xAxis, 0, 1023, -255, 255);
  */

   int leftSpeed = Speed - turn;
   int rightSpeed = Speed + turn;
   
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
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
   }
   
    else {
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    }


 
  analogWrite(enA, abs(rightSpeed)); // Send PWM signal to motor A
  analogWrite(enB, abs(leftSpeed)); // Send PWM signal to motor B
  Serial.println(leftSpeed); 
  Serial.println(rightSpeed); 
  Serial.println(x); 


}
