//This code was upload to Atmega168 (arduino nano clone) microntroler.
//8 pin on arduino was conected to HF3FF subminature power relay control leg.
//second control leg was connect to GND on arduino
//Two circut legs was connected to lamp wire.


#define LIGHT_SWITCH 8

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LIGHT_SWITCH, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    char order = Serial.read();
    //int order = Serial.readString().toInt();
    switch(order){
      case '1':
        digitalWrite(LIGHT_SWITCH, HIGH);
        break;
      case '0':
        digitalWrite(LIGHT_SWITCH, LOW);
        break;
      default:
        Serial.println("Wrong command");
        Serial.println(order);
        break;
    }
  }
}