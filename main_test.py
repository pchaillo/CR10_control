#!/usr/bin/env python3
        
# -*- coding: utf-8 -*-
"""
Created on 22/08/2022

@author: pchaillo

Script to use Creality CR10 printer as a test platform
"""

# import CR10Lib as CR10
# CR10.home()
import matplotlib.pyplot as plt
import time
import CR10_Duino as CR10_test
import HG_C1100_P as ls
import RubberSensor as rs
#import csv
#import ResistorLenght as RL

#initialiser les capteurs 
lasensor=ls.SerialDuino()
rubsensor=rs.RubberSerialDuino()


#plot




#initialiser les listes
pourc_resistor_t,pourc_resistor_c,printer_strain_t,sensor_strain_t,printer_strain_c,sensor_strain_c,resistor_t,resistor_c=[],[],[],[],[],[],[],[]

#printer move functions

#to do the up movement
def Upz(z):
 X = 0
 Y = 100
 printer.driveToPosition(X,Y,z)

#to do the down movement
def Downz(z):
 X = 0
 Y = 100
 printer.driveToPosition(X,Y,z)

#pour aller au position de depart
def first(z):
 X = 0
 Y = 100
 printer.driveToPosition(X,Y,z)

 #time.sleep(40)
 
# define a function that reads from the laser sensor
def laserRead(z1,lo):
    lasensor.UpdateSensors()
    strain = lasensor.Calcul_Strain(z1,lo)
    return strain
    
# define a function that reads from the rubber sensor
def RubberRead():
    rubsensor.UpdateSensors()
    res = rubsensor.GetRes()
    return res
    
# to do the traction test 
def traction(zmin,zmax,step,zs,lo,Ro):
  #RL.Real_Plot()
  
  for z in range(zmin,zmax,step):
   Upz(z)
   printer_strain_t.append(((z-zmin)/zmin)*100)
   sensor_strain_t.append(laserRead(zs,lo))
   resistor_t.append(RubberRead())
   pourc_resistor_t.append(round(((RubberRead()-Ro)*100)/Ro,1))
   time.sleep(2)
   
#def CheckLogic(arr):
    
    #for i in range(len(arr)):
        #if arr[i]>=arr[i+1]:
            #arr[i]=arr[i+1]
            

# to do the compression test   
def compression(zmax,zmin,step,zs,lo,Ro):
  for z in reversed(range(zmin,zmax,step)):
   Downz(z)
   print(z)
   printer_strain_c.append(((z-zmin)/zmin)*100)
   sensor_strain_c.append(laserRead(zs,lo))
   resistor_c.append(RubberRead())
   pourc_resistor_c.append(round(((RubberRead()-Ro)*100)/Ro,1))
   time.sleep(2)
   print(z)
      

#height=20

#initialiser le printer
printer = CR10_test.SerialDuino()
time.sleep(2)

#go to the home and purge
printer.home()
printer.purgeSerial()

#go to the first point and put the sensor in the correct place
first(50)
pause=input("if you want to continue,click on any button")
lo=float(input("put the initial lenght of the sensor"))
lasensor.UpdateSensors()
zs= lasensor.GetDist()
Ro=RubberRead()
traction(50,80,1,zs,lo,Ro)
time.sleep(2)
compression(80,50,1,zs,lo,Ro)
# set the labels of the plot
plt.xlabel('strain(%)')
plt.ylabel('resistance (ohm)')
plt.title('resistance versus Time')

plt.subplot(121)
plt.plot(sensor_strain_t,resistor_t,color='black', linewidth = 1,
         marker='o', markerfacecolor='black', markersize=3)
plt.plot(sensor_strain_c,resistor_c,color='red', linewidth = 1,
         marker='o', markerfacecolor='red', markersize=3)
plt.xlabel('laser_strain(%)')
plt.ylabel('resistance (ohm)')
plt.subplot(122)
plt.plot(printer_strain_t,resistor_t,color='black', linewidth = 1,
         marker='o', markerfacecolor='black', markersize=3, label="traction")
plt.plot(printer_strain_c,resistor_c,color='red', linewidth = 1,
         marker='o', markerfacecolor='red', markersize=3,label="repulsion")
plt.xlabel('printer_strain(%)')
plt.ylabel('resistance (ohm)')

plt.subplot(131)
plt.plot(t,resistor_t,color='black', linewidth = 1,
         marker='o', markerfacecolor='black', markersize=3)

plt.xlabel('time(sec)')
plt.ylabel('resistance (ohm)')

plt.legend()
plt.show()
#Position = height
#printer.driveToHeight(Position)
#time.sleep(120)#to put the basessss
########




