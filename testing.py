#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:03:16 2023

@author: yehya
"""
import HG_C1100_P as ls
import RubberSensor as rs
import time
import CR10_Duino as CR10_test
import time
lasensor=ls.SerialDuino()
rubsensor=rs.RubberSerialDuino()
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
def laserRead(z1,lo):
    lasensor.UpdateSensors()
    strain = lasensor.GetDist()
    return strain

def RubberRead():
    rubsensor.UpdateSensors()
    res = rubsensor.GetRes()
    return res

# to do the traction test 
def traction(zmin,zmax,step,zs,lo):
  #RL.Real_Plot()
  
  for z in range(zmin,zmax,step):
   Upz(z)
  # printer_strain_t.append(z-zmin)
   printer_strain_t.append(z)
   sensor_strain_t.append(laserRead(zs,lo))
   #resistor_t.append(RubberRead())
   time.sleep(1)
   
#def CheckLogic(arr):
    
    #for i in range(len(arr)):
        #if arr[i]>=arr[i+1]:
            #arr[i]=arr[i+1]
            

# to do the compression test   
def compression(zmax,zmin,step,zs,lo):
  
  for z in reversed(range(zmin,zmax,step)):
   Downz(z)
   #printer_strain_c.append(z-zmin)
   printer_strain_c.append(z)
   sensor_strain_c.append(laserRead(zs,lo))
   #resistor_c.append(RubberRead())
   time.sleep(1)

sensor_strain_t,sensor_strain_c,printer_strain_t,printer_strain_c=[],[] ,[],[]   
printer = CR10_test.SerialDuino()
time.sleep(1)

#go to the home and purge
printer.home()
printer.purgeSerial()

#go to the first point and put the sensor in the correct place
first(50)
pause=input("if you want to continue,click on any button")
zs=float(input("put the value represented on the sensor: "))
lo=float(input("put the initial lenght of the sensor"))
traction(50,80,1,zs,lo)
time.sleep(1)
compression(80,50,1,zs,lo)      