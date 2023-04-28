#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:07:10 2023

@author: yehya
"""
import matplotlib.pyplot as plt
# set the labels of the plot
plt.xlabel('strain(%)')
plt.ylabel('resistance (ohm)')
plt.title('resistance versus Time')

#initialiser les listes
printer_strain_t,sensor_strain_t,printer_strain_c,sensor_strain_c,resistor_t,resistor_c=[],[],[],[],[],[]
printer_strain_c=[24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
printer_strain_t=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
resistor_c=[2.08, 2.14, 2.14, 2.15, 2.19, 2.33, 2.31, 2.28, 2.36, 2.4, 2.38, 2.43, 2.38, 2.52, 2.54, 2.57, 2.52, 2.49, 2.49, 2.48, 2.46, 2.4, 2.34, 2.25, 2.06]
resistor_t=[1.9, 2.06, 2.05, 2.14, 2.19, 2.22, 2.24, 2.25, 2.25, 2.16, 2.22, 2.24, 2.22, 2.19, 2.19, 2.18, 2.16, 2.15, 2.09, 2.21, 2.14, 2.14, 2.21, 2.11, 2.14]
sensor_strain_c=[20.16, 20.02, 18.93, 18.34, 17.11, 15.94, 14.8, 14.16, 12.96, 11.74, 11.01, 9.97, 8.73, 7.61, 6.99, 5.7, 4.59, 3.85, 2.69, 1.46, 0.74, 0.34, 1.53, 1.82, 1.02]
sensor_strain_t=[0.0, 0.3, 1.02, 2.19, 1.13, 0.06, 0.68, 1.88, 3.09, 3.79, 4.87, 6.12, 7.34, 7.88, 9.1, 10.27, 10.91, 12.01, 13.24, 14.04, 15.05, 16.31, 17.47, 18.19, 19.19]
plt.subplot(121)
a=round(resistor_c[1],1)
print(a)
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
plt.legend()
plt.show()