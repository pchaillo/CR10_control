#import Printer_Arduino as Arduino
import time
import CR10_Duino as Slider
#Ard.Put_Arduino_Parameters()

slider = Slider.SerialDuino()
time.sleep(2)
print("HELLO!")
print("I hope you're fine!!!")
print("You can control me securely and correctly if you follow the instructions bellow:\n1. To move to the specified position,click on P\n2.To reset me to my home position(0,0,0),click on:H\n3.To stop me,click on S")
user=input("Put your order:")
if user=="P":
 

