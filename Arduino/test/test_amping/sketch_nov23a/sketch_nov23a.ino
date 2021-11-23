const unsigned int MAX_MESSAGE_LENGTH = 12;
String command;
int x = 0;

void setup() {
 Serial.begin(9600);
 Serial.setTimeout(100);
}

void loop() {

 //Check to see if anything is available in the serial receive buffer
   while (Serial.available() > 0){
    
    x = x+1;
    Serial.println(x);
     int Head = Serial.parseInt();
     int Speed = Serial.parseInt();
     int Turn = Serial.parseInt();
     
     Serial.println("Head");
     Serial.println(Head);
     Serial.println("Speed");
     Serial.println(Speed);
     Serial.println("Turn");
     Serial.println(Turn);
     
     if (Serial.available()) {
      command = Serial.readStringUntil('\n');
      command.trim();
      Serial.println("Left over");
      Serial.println(command);
      }
 }
 }
