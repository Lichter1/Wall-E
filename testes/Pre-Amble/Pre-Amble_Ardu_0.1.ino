String command;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.println("Start"); 
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
   // Serial.println();
    command = Serial.readStringUntil('\n');
    command.trim();
    command = "Raspbeery pi Command: " + command;
    Serial.println(command);
    Serial.println("Start");  
  }}
