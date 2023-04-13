#define RESISTOR 10000 //This should be the same value of the used resistor  
#define RUBBERCORDPIN A0  //This is the pin where the cord is connected tp
int value; 
int vin = 5;          // Store input voltage, this should be 5 
float vout = 0;        // Store output voltage 
float refresistor1 = 10;  // Variable to store the R1 value 
float refresistor2 = 0;  //  Value is determined by the voltage 
float ReadingResistor=0;
//----------------------------------------------------------------
float SumA0 = 0;
float OffsetA0 = 0;
float WindowSize = 20;
float WindowSizeBegin = 200;
float WindowSizeBackup;
float NStartSkipFrames = 100;
float SkipFramesCounter = 0;
int Counter = 0;
bool Beginning = true;
//----------------------------------------------------------------
float RubberSensorReading()
{
  value = analogRead(RUBBERCORDPIN);     //Read the value                                           //Just like we did earlier
  vout = (5.0 / 1023.0) * value;         // Calculates the voltage 
  refresistor2=(vout/(vin-vout))*refresistor1;
  return refresistor2;
}

//----------------------------------------------------------------
void setup() {
  // put your setup code here, to run once:
   Serial.begin(115200); 
}

void loop() {
  // put your main code here, to run repeatedly:
  
  float AZero = analogRead(A1);
  SumA0 += AZero;

  Counter++;

  if (Counter >= WindowSize)
  {
    float MeanA0 = SumA0 / WindowSize;    
    float DistInMM = (MeanA0/1023)*70 - 35 + 0.18; // Convert to mm and adjust with a small factor to match readings from display on the backside of the device
    //Serial.print(MeanA0);
    //Serial.print(",");
    Serial.print(DistInMM);
    Serial.print(";");
    ReadingResistor=RubberSensorReading();
    delay(10);
    Serial.println(ReadingResistor);
    delay(10);
    Counter = 0;
    SumA0 = 0;
    Serial.flush();
    delay(1000);   
  }
  

}
