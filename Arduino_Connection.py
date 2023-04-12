#!/usr/bin/env python3
        
# -*- coding: utf-8 -*-
"""
Created on 22/08/2022

@author: Yehya SHARIF

Script to use Creality CR10 printer as a test platform
"""

import time
import CR10_Duino as CR10_test
import serial as sr
import numpy as np
import matplotlib.pyplot as plt
class Arduino:
 def __init__(self):
  self.Port=''
  self.BaudRate=''
 def Put_Arduino_Parameters(self): 
  print(" Hello! \nI'm Arduino,if you want to connect me,please specify the port serial connection and the BaudRate")
  print("You can find my port using device manager on Windows operating system  : Device Manager --> Ports(COM & LPT) \n or u can find it in arduino IDE: Tools --> Port on Ubuntu OS (it can be /dev/ttyACM0)")
   print("Don't Forget to connect me ;)")
  self.Port = input(" Enter the Port: ")
  self.Baudrate =int( input(" Enter the Baudrate: "))
  arduino=sr.Serial(self.Port,self.Baudrate)#create an instance arduino from the serial class
arduino=Arduino()
arduino.Put_Arduino_Parameters()




