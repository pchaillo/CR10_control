#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:07:58 2023

@author: yehya
"""
import matplotlib.pyplot as plt

sensor_strain_t=[ 0.1, 1.33, 3.11, 3.91, 5.16, 6.28, 7.09, 8.11, 9.31, 10.57, 11.2, 12.41, 13.56, 14.37, 15.4, 16.51, 17.68, 18.41, 19.59]
resistor_t=[1.91, 2.05, 2.16, 2.18, 2.18, 2.16, 2.14, 2.14, 2.12, 2.11, 2.14, 2.09, 2.08, 2.06, 2.06, 2.06, 2.06, 2.05, 2.05]
sensor_strain_c=[20.4, 20.32, 19.23, 18.48, 17.38, 16.17, 14.44, 13.18, 12.01, 11.34, 10.17, 8.92, 8.25, 7.09, 5.9, 4.73, 3.91, 2.74, 1.58, 0.83, 0.27]
resistor_c=[2.01, 2.04, 2.11, 2.08, 2.12,2.18, 2.22, 2.27, 2.33, 2.27, 2.34, 2.37, 2.24, 2.37, 2.38, 2.37, 2.37, 2.42, 2.33, 2.31, 2.43]
plt.plot(sensor_strain_t,resistor_t,color='black', linewidth = 1,
         marker='o', markerfacecolor='black', markersize=3)
plt.plot(sensor_strain_c,resistor_c,color='red', linewidth = 1,
         marker='o', markerfacecolor='red', markersize=3)

plt.grid()
plt.show()