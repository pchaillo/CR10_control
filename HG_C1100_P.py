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
        self.port = '/dev/ttyACM0'
        self.baud = 115200

        #INIT
        self.dist = 0
        self.ser = serial.Serial(self.port,self.baud) 

    def UpdateSensors(self):

        ligne_raw = str(self.ser.readline())
        # print(ligne_raw)

        ligne_cut = ligne_raw.split("'")
        ligne_cut2 = ligne_cut[1].split("\\")
       

        print(ligne_cut2) # for debug

        try:
            self.dist = float(ligne_cut2[0])

        except:
            print('Attention, lecture impossible')
            a = 0

    def GetDist(self):
        # print(str(self._pres)) # for debug

        
        return self.dist
        
    def Calcul_Strain(self,z1):
       lo=83
       z2 = abs(self.GetDist())
       deltaz= abs(z1-z2)
       return deltaz*100/lo   


