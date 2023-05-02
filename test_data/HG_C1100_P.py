#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:23:53 2022

@author: pchaillo
"""

import serial
import time


class SerialDuino:

    def __init__(self):
        # PARAM7TRES
        self.port = '/dev/ttyACM1'
        self.baud = 115200

        #INIT
        self.dist = 0
        self.ser = serial.Serial(self.port,self.baud) 

    def UpdateSensors(self):
        #flushing
        self.ser.flush()
        self.ser.flushInput()
        self.ser.flushOutput()
        time.sleep(0.1)
        #------------------------------
        ligne_raw = str(self.ser.readline())
        # print(ligne_raw)

        ligne_cut = ligne_raw.split("'")
        ligne_cut2 = ligne_cut[1].split("\\")
        ligne_cut3 = ligne_cut2[0].split(";")

        #print(ligne_cut3[0]) # for debug

        try:
            self.dist = float(ligne_cut3[1])

        except:
            print('Attention, lecture impossible')
            a = 0

    def GetDist(self):
        # print(str(self._pres)) # for debug

        
        return self.dist
        
    def Calcul_Strain(self,z1,lo):
       z2 = abs(self.GetDist())
       deltaz= abs(z1-z2)
       return round(deltaz*100/lo,2)   
    
#rubsensor=SerialDuino()
#while(1):
    #rubsensor.UpdateSensors()
    #res = rubsensor.Calcul_Strain(2.29,94)
    #print(res)
