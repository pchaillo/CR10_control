import time
import CR10_Duino as CR10_test
import serial as sr
import numpy as np
import matplotlib.pyplot as plt

arduino=sr.Serial('COM3',9600)#create an instance arduino from the serial class

plt.close('all')
plt.figure()
plt.ion()
plt.xlabel('Lenght')
plt.ylabel('Resistance(Kohm)')
plt.show()
XY=np.array([])

printer=CR10_test.SerialDuino() #create an instance from serialduino class
time.sleep(2)
printer.home()
currpos=0
firstpos=printer.getCurrentPosition()# give the first posiion as [x0,y0,z0]
firstZ=firstpos[2] #the current first z
print(firstZ)#TO SHOW THE CURRENT POSITION TO THE USER
lastZ = int(input("Enter the last Z that you want(the first Z must be lower than the last Z):")) #the last Z specified
#The sensor  will be tested only on Z axis
for i in range(firstZ,lastZ):
  #printer.driveToHeight(height)
  printer.driveToPosition(0,0,firstZ+i)#to drive to the position[0,0,height]
  ardInfo=arduino.readline()
  ardInfo.decode()
  resistor=float(ardInfo[0:4])
  currpos=printer.getCurrentPosition()
  length=currpos[2]
  plt.cla()
  plt.plot(length,resistor)
  plt.pause(0.000001)
  # voltage=float(a[4:6])
for j in reversed(range(firstZ,lastZ)):
  #printer.driveToHeight(height)
  printer.driveToPosition(0,0,lastZ-j)#to drive to the position[0,0,height]
  ardInfo=arduino.readline()
  ardInfo.decode()
  resistor=float(ardInfo[0:4])
  currpos=printer.getCurrentPosition()
  length=currpos[2]
  plt.cla()
  plt.plot(length,resistor)
  plt.pause(0.000001)

  # voltage=float(a[4:6])
arduino.close()


