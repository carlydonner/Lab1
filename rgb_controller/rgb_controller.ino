
#define ledR 3
#define ledG 5 
#define ledB 6
#define pot_pin A0
 
void setup(){
  Serial.begin(9600); //baud rate
}

void loop(){
  int val;
  val = analogRead(pot_pin);
  analogWrite(ledR, val/4); //ranges from 0 to 1024, res 4.9 mV
  Serial.print(val);
}
