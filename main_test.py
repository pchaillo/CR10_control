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

def Upz():
 X = 0
 Y = 100
 Z = 100
 printer.driveToPosition(X,Y,Z)
def Downz():
 X = 0
 Y = 100
 Z = 60
 printer.driveToPosition(X,Y,Z)
def first():
 X = 0
 Y = 100
 Z = 70
 printer.driveToPosition(X,Y,Z)
 #time.sleep(40)
 #X = 0
 #Y = 100
 #Z = 50
 #printer.driveToPosition(X,Y,Z)

#height=20

printer = CR10_test.SerialDuino()
time.sleep(2)
printer.home()
printer.purgeSerial()

#Position = height
#printer.driveToHeight(Position)
#time.sleep(120)#to put the base

first()
time.sleep(10)
#the testing will start
for i in range(4):
	Upz()
	Downz()

