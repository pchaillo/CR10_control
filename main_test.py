#!/usr/bin/env python3
        
# -*- coding: utf-8 -*-
"""
Created on 22/08/2022

@author: pchaillo

Script to use Creality CR10 printer as a test platform
"""

# import CR10Lib as CR10
# CR10.home()

import time
import CR10_Duino as CR10_test
import HG_C1100_P as ls
import RubberSensor as rs
#import csv
#import ResistorLenght as RL


def Upz(z):
 X = 0
 Y = 100
 printer.driveToPosition(X,Y,z)

def Downz(z):
 X = 0
 Y = 100
 printer.driveToPosition(X,Y,z)
 
def first(z):
 X = 0
 Y = 100
 printer.driveToPosition(X,Y,z)

 #time.sleep(40)

 #X = 0
 #Y = 100
 #Z = 50
 #printer.driveToPosition(X,Y,Z)

 
def traction(zmin,zmax,step):
  #RL.Real_Plot()
  for z in range(zmin,zmax,step):
   Upz(z)
   time.sleep(1)
   
def compression(zmax,zmin,step):
  for z in reversed(range(zmin,zmax,step)):
   Downz(z)
   time.sleep(1)   

#height=20

printer = CR10_test.SerialDuino()
#printer.purgeSerial()
printer.home()
printer.purgeSerial()

first(70)
#time.sleep(10)
#traction(70,105,5)
#time.sleep(1)
#compression(105,70,5)

#Position = height
#printer.driveToHeight(Position)
#time.sleep(120)#to put the base




