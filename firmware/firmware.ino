const int BTN = 4;
bool ledOn = false;        // remembers ON/OFF
int lastState = HIGH;      // button state last loop

void setup() {
  Serial.begin(115200);
  pinMode(BTN, INPUT_PULLUP);
}

void loop() {
  int state = digitalRead(BTN);
  if (lastState == HIGH && state == LOW) {  // just pressed
    ledOn = !ledOn;                         // flip true/false
    Serial.println(ledOn ? "ON" : "OFF");
  }
  lastState = state;

  if (ledOn) rgbLedWrite(RGB_BUILTIN, 0, 50, 0);
  else       rgbLedWrite(RGB_BUILTIN, 0, 0, 0);
  delay(30);   // also stops "bounce" (one press counted twice)
}