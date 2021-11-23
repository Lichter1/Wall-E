#define enA 11
#define in1 10
#define in2 9
#define enB 6
#define in3 8
#define in4 7
int Speed = 0;
void setup() {
  Serial.begin(9600);
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
  // Y-axis used for forward and backward control
  
 Speed = map(yAxis, 0, 1023, -255, 255);
 Serial.println(xAxis);
 Serial.println(Speed);
}
