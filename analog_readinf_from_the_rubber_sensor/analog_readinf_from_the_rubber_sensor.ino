#define RESISTOR 10000 //This should be the same value of the used resistor  
#define RUBBERCORDPIN A0  //This is the pin where the cord is connected tp
int value; 
int vin = 5;          // Store input voltage, this should be 5 
float vout = 0;        // Store output voltage 
float refresistor1 = 10;  // Variable to store the R1 value 
float refresistor2 = 0;  //  Value is determined by the voltage 
char userInput=' ';
void setup(void) { 
     Serial.begin(115200); 
     //Serial.println("voltage,resistor");
   } 
void loop(void) { 

       value = analogRead(RUBBERCORDPIN);     //Read the value
                                             //Just like we did earlier
       vout = (5.0 / 1023.0) * value;         // Calculates the voltage 
       refresistor2=(vout/(vin-vout))*refresistor1;
       // Outputs the information 
       //Serial.println(vout);
       //Serial.print(",");
       Serial.println(refresistor2);
       //Serial.print(vout);
       Serial.flush();
       //delay(300);
       delay(1000);
 }   
   
