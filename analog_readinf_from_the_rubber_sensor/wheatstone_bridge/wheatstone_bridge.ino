#define RESISTOR A3 //This should be the same value of the used resistor  
#define RUBBERCORDPIN A0  //This is the pin where the cord is connected tp
int value; 
int vin = 5;          // Store input voltage, this should be 5 
float vout = 0;        // Store output voltage 
float refresistor1 = 10;  // Variable to store the R1 value 
float refresistor2 = 0;  //  Value is determined by the voltage 
char userInput=' ';
void setup() {
   Serial.begin(115200); 
     //Serial.println("voltage,resistor");
}

void loop() {
  float vc=(5.1 / 1023.0)*analogRead(RESISTOR); 
  float vd=(5.1 / 1023.0)*analogRead(RUBBERCORDPIN);
  float vdc=vd-vc;
  Serial.println(vdc);
  delay(10);
  //Serial.print(vout);
  Serial.flush();
}
