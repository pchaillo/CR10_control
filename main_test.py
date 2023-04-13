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
# set the labels of the plot
plt.xlabel('strain(%)')
plt.ylabel('resistance (ohm)')
plt.title('resistance versus Time')
#initialiser les listes
printer_strain,sensor_strain,resistor=[],[],[]

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
def laserRead(z1):
    lasensor.UpdateSensors()
    strain = lasensor.Calcul_Strain(z1)
    return strain
    
# define a function that reads from the rubber sensor
def RubberRead():
    rubsensor.UpdateSensors()
    res = rubsensor.GetRes()
    return res
    
# to do the traction test 
def traction(zmin,zmax,step,zs):
  #RL.Real_Plot()
  for z in range(zmin,zmax,step):
   Upz(z)
   #printer_strain.append(z)
   sensor_strain.append(laserRead(zs))
   resistor.append(RubberRead())
   time.sleep(1)
  

# to do the compression test   
def compression(zmax,zmin,step,zs):
  for z in reversed(range(zmin,zmax,step)):
   Downz(z)
   #printer_strain.append(z)
   sensor_strain.append(laserRead(zs))
   resistor.append(RubberRead())
   time.sleep(1)
      

#height=20

#initialiser le printer
printer = CR10_test.SerialDuino()
time.sleep(2)

#go to the home and purge
printer.home()
printer.purgeSerial()

#go to the first point and put the sensor in the correct place
first(70)
pause=input("if you want to continue,click on any button")
zs=float(input("put the value represented on the sensor: "))
traction(70,105,3,zs)
time.sleep(1)
compression(105,70,3,zs)

#print(printer_strain)
print(sensor_strain)
print(resistor)
plt.plot(sensor_strain,resistor,color='red', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=3)
plt.show()
#Position = height
#printer.driveToHeight(Position)
#time.sleep(120)#to put the base




