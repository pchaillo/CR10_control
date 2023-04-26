#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:03:16 2023

@author: yehya
"""
import HG_C1100_P as ls
import RubberSensor as rs
import time
lasensor=ls.SerialDuino()
rubsensor=rs.RubberSerialDuino()

def laserRead(z1,lo):
    lasensor.UpdateSensors()
    strain = lasensor.Calcul_Strain(z1,lo)
    return strain

def RubberRead():
    rubsensor.UpdateSensors()
    res = rubsensor.GetRes()
    return res
sensor_strain_t,resistor_t=[],[]

#for z in range(80,105,2):
while(1):
    #deplacement
    time.sleep(1)
    print(laserRead(1.94,94))
    print(RubberRead())
    # sensor_strain_t.append(laserRead(1.94,94))
    # resistor_t.append(RubberRead())
    # 
    # sensor_strain_t.append(laserRead(1.94,94))
    # resistor_t.append(RubberRead())
    # time.sleep(1000)
    
    #l=laserRead(1.94,94)
    #r=RubberRead()
    #print(l)
    #print(r)
    