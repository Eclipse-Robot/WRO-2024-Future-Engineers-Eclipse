#include <Servo.h>
int analogPin = A0;
int outputPin = 3;
int inputValue = 0;
int Speed = 0;
int Direction = 1;
int Angle = 0;
int motor1pin1 = 4;
int motor1pin2 = 5;
int servoPin = 6; 
Servo Servo1;
String inputString = "";
boolean stringComplete = false;

void setup() {
  Servo1.attach(servoPin);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(outputPin, OUTPUT);
  digitalWrite(outputPin, HIGH);
  Serial.begin(9600);

  // Wait for the serial port to connect. Needed for native USB
  // while (!Serial) { ; }

  while (Serial.available() <= 0) {
    sendStatus();
    delay(300);
  }
}

void loop() {
  // Ensure SerialEvent() gets called
  if (Serial.available()) {
    SerialEvent();
  }

  if (stringComplete) {
    if (inputString.startsWith("status")) {
      sendStatus();
    } else if (inputString.startsWith("Speed")) {
      Speed = inputString.substring(5).toInt();
    } else if (inputString.startsWith("Direction")) {
      Direction = inputString.substring(9).toInt();
    } else if (inputString.startsWith("Steering")) {
      // Angle between 0 and 180 degrees for servo motor
      Angle = inputString.substring(8).toInt();
    } else {
      Serial.println("invalid command");
    }

    // Reset string
    stringComplete = false;
    inputString = "";
  }
 
  // Controlling speed (0 = off and 255 = max speed)
  analogWrite(10, Speed); // ENB pin
  Forward_Backward();
  Servo1.write(Angle);
  
  delay(10);
}

void sendStatus() {
  char buffer[50];
  inputValue = analogRead(analogPin);
  sprintf(buffer, "Analog input %d is %d", analogPin, inputValue);
  Serial.println(buffer);
}

void Forward_Backward() {
  if (Direction == 1) {
    digitalWrite(motor1pin1, HIGH);
    digitalWrite(motor1pin2, LOW);
  } else if (Direction == 2) {
    digitalWrite(motor1pin1, LOW);
    digitalWrite(motor1pin2, HIGH);
  } else {
    Serial.println("invalid direction");
  }
}

void SerialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
