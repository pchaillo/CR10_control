#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:49:51 2023

@author: yehya
"""

import matplotlib.pyplot as plt
from scipy import stats

time=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
#test1 lists
pourc_resistor_c_1 = [52.4, 52.4, 57.1, 59.5, 59.5, 66.7, 73.8, 73.8, 76.2, 77.4, 81.0, 81.0, 84.5, 85.7, 85.7, 86.9, 85.7, 85.7, 84.5, 82.1, 79.8, 76.2, 73.8, 65.5, 58.3, 51.2, 40.5, 27.4, 17.9, 9.5]
pourc_resistor_t_1 = [0, 9.5, 17.9, 28.6, 35.7, 41.7, 45.2, 47.6, 51.2, 51.2, 53.6, 57.1, 54.8, 54.8, 54.8, 57.1, 57.1, 57.1, 57.1, 57.1, 57.1, 48.8, 57.1, 57.1, 54.8, 57.1, 57.1, 54.8, 57.1, 54.8]
printer_strain_c_1 = [58, 56, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0, 38.0, 36.0, 34.0, 32.0, 30.0, 28, 26.0, 24.0, 22.0, 20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0, 4.0, 2.0, 0.0]
printer_strain_t_1 =[0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58]
resistor_c_1= [1.29, 1.29, 1.32, 1.35, 1.38, 1.4, 1.44, 1.47, 1.48, 1.51, 1.51, 1.51, 1.56, 1.59, 1.59, 1.57, 1.59, 1.57, 1.56, 1.59, 1.52, 1.49, 1.44, 1.4, 1.35, 1.27, 1.18, 1.08, 1.0, 0.93]
resistor_t_1=[0.86, 0.93, 0.99, 1.07, 1.13, 1.2, 1.25, 1.25, 1.27, 1.33, 1.29, 1.3, 1.3, 1.29, 1.32, 1.32, 1.33, 1.32, 1.32, 1.32, 1.35, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.3, 1.32, 1.3]
printer_strain_t_linear_1 =[0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
resistor_t_linear_1=[0.86, 0.93, 0.99, 1.07, 1.13, 1.2, 1.25]
#characteristics calculation functions

def hysterisis_calculation(physical_forward,physical_backward,electrical_forward,electrical_backward):
    #function that calculate the hysterisi error pourcentage
    diff=[None]*len(physical_forward)
    New_list = electrical_backward.copy()
    New_list.reverse()
    for i in range(len(physical_forward)):
        diff[i]=abs(electrical_forward[i]-New_list[i])
    max_diff=max(diff)
    max_loading_res=max(electrical_forward)
    percentage=(max_diff*100)/max_loading_res
    max_index=diff.index(max_diff)    
    return diff,percentage,max_index
 

def linearity(physical,electrical):
    
    plt.scatter(physical,electrical)
    slope, intercept, r, p, std_err = stats.linregress(physical,electrical)
    linear_function=[None]*len(physical)
    linear_error=[None]*len(physical)
    for i in range(len(physical)):
     linear_function[i]= slope * physical[i] + intercept
     linear_error[i]=abs(linear_function[i]-electrical[i])
    max_error=max(linear_error)
    output_full_range=max(electrical)
    linear_err=(max_error/output_full_range)*100
    plt.scatter(physical,electrical)
    plt.plot(physical, linear_function)
    plt.show()
    return linear_error,linear_err    
    
    
    
    
    
    
    
diff_1,hyst_1,max_index_1 =hysterisis_calculation(printer_strain_t_1,printer_strain_c_1,resistor_t_1, resistor_c_1)
linearity_list,linearity_1=linearity(printer_strain_t_linear_1,resistor_t_linear_1)