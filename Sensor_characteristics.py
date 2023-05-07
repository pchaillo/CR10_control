#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:49:51 2023

@author: yehya
"""

import matplotlib.pyplot as plt
from scipy import stats
from itertools import chain
import RubberSensor as rs #to measure the accuracy and the precision

rubsensor=rs.RubberSerialDuino()

time=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
#test1 lists
pourc_resistor_c_1 = [52.4, 52.4, 57.1, 59.5, 59.5, 66.7, 73.8, 73.8, 76.2, 77.4, 81.0, 81.0, 84.5, 85.7, 85.7, 86.9, 85.7, 85.7, 84.5, 82.1, 79.8, 76.2, 73.8, 65.5, 58.3, 51.2, 40.5, 27.4, 17.9, 9.5]
pourc_resistor_t_1 = [0, 9.5, 17.9, 28.6, 35.7, 41.7, 45.2, 47.6, 51.2, 51.2, 53.6, 57.1, 54.8, 54.8, 54.8, 57.1, 57.1, 57.1, 57.1, 57.1, 57.1, 48.8, 57.1, 57.1, 54.8, 57.1, 57.1, 54.8, 57.1, 54.8]
printer_strain_c_1 = [58, 56, 54.0, 52.0, 50.0, 48.0, 46.0, 44.0, 42.0, 40.0, 38.0, 36.0, 34.0, 32.0, 30.0, 28, 26.0, 24.0, 22.0, 20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0, 4.0, 2.0, 0.0]
printer_strain_t_1 =[0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58]
resistor_c_1= [1.29, 1.29, 1.32, 1.35, 1.38, 1.4, 1.44, 1.47, 1.48, 1.51, 1.51, 1.51, 1.56, 1.59, 1.59, 1.59, 1.59, 1.57, 1.56, 1.54, 1.52, 1.49, 1.44, 1.4, 1.35, 1.27, 1.18, 1.08, 1.0, 0.93]
resistor_t_1=[0.86, 0.93, 0.99, 1.07, 1.13, 1.2, 1.25, 1.25, 1.27, 1.28, 1.29, 1.3, 1.3, 1.29, 1.32, 1.32, 1.3, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.3, 1.32, 1.3]
printer_strain_t_linear_1 =[0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0]
resistor_t_linear_1=[0.86, 0.93, 0.99, 1.07, 1.13, 1.2, 1.25, 1.25, 1.27, 1.28, 1.29, 1.3, 1.3, 1.29, 1.32, 1.32]
#inputs of accuracy function
lenght_1=57.1 #in mm
res_data_sheet_1=0.786 #kohm
lenght_2=81.2
res_data_sheet_2=1.119
#characteristics calculation functions

def hysterisis_calculation(physical_forward,physical_backward,electrical_forward,electrical_backward):
    
    """
    This function takes four inputs (physical_forward,physical_backward,electrical_forward,electrical_backward) and return:
        1. diff:the difference list between the backward and forward value of the electrical list
        2. percentage: the maximum hysterisis percentange
        3. the average hysterisis
    and plot the measured value in forward and backward direction to visualize the hysterisis curve
    
    """
    
    diff=[None]*len(physical_forward)# define the difference list
    
    #reverse the electrical backward list
    New_list = electrical_backward.copy()
    New_list.reverse()
    #------------------------------------
    
    sum_diff=0 #this variable to be used in the average value
    
    #to calculate the difference list and the sum variable
    for i in range(len(physical_forward)):
        diff[i]=abs(electrical_forward[i]-New_list[i])
        sum_diff=sum_diff+diff[i]
    #-----------------------------------    
    
    #calculate the average sum of the diff list to be used in average hysteris formula
    avg_sum_diff=sum_diff/len(diff)
    max_diff=max(diff)
    #-------------------------------------
    
    #calculate the maximmum and the minimum boundaries of the output electrical range
    max_loading_res=max(chain(electrical_forward,electrical_backward))
    min_loading_res=min(chain(electrical_forward,electrical_backward))
    output_electrical_range=(max_loading_res-min_loading_res)
    #----------------------------------------
    
    
    percentage=(max_diff*100)/output_electrical_range
    avg_hysterisis=(avg_sum_diff*100)/output_electrical_range
    max_index=diff.index(max_diff)    
    
    #plot the hysterisis graph
    plt.plot(physical_forward,electrical_forward,color='black', linewidth = 1,
             marker='o', markerfacecolor='black', markersize=3)
    plt.plot(physical_backward,electrical_backward,color='black', linewidth = 1,
             marker='o', markerfacecolor='black', markersize=3)
    plt.show()
    #----------------------------------------
    
    return diff,percentage,max_index,avg_hysterisis
 

def linearity_error(physical,electrical):
    
    """
    This function takes two inputs (physical,electrical) and return:
        1. linear_error_list:the difference list between the linear regression and the actual measured value of the electrical list
        2. linear_err: the non_linearity error percentage between the linear one and the actual one
        3. slope: sensitivity of the linear regression function
        
    """
    slope, intercept, r, p, std_err = stats.linregress(physical,electrical)
    linear_function=[None]*len(physical)
    linear_error_list=[None]*len(physical)
    for i in range(len(physical)):
     linear_function[i]= slope * physical[i]+intercept
     linear_error_list[i]=abs(linear_function[i]-electrical[i])
    max_error=max(linear_error_list)
    output_full_range=max(electrical)-min(electrical)
    linear_err=(max_error/output_full_range)*100
    plt.plot(physical,electrical,color='black', linewidth = 1,
             marker='o', markerfacecolor='black', markersize=3)
    plt.plot(physical, linear_function)
    plt.show()
    return linear_error_list,linear_err,slope    
       
def non_linearity_error(physical,electrical):
    
    """
    This function takes two inputs (physical,electrical) and return:
        1. error_list:the difference list between the linear and the actual measured value of the electrical list
        2. max_error: the non_linearity error percentage between the linear one and the actual one
        3. slope: sensitivity of the linear function
    and plot the measured value with the linear value to visualize the linearity error
    
    """
    #define the list used in the program
    error_list=[None]*len(physical)
    linear_function=[None]*len(electrical)
    
    #define the slope of the linear function
    slope=(max(electrical)-electrical[0])/(physical[len(physical)-1])
    
    #calculate the error list and the linear function
    for i in range(len(physical)):
     linear_function[i]= slope * physical[i]+electrical[0]
     error_list[i]=(abs(linear_function[i]-electrical[i])*100)/(max(electrical)-electrical[0])
     
    #the non_linearity error percentage between the linear one and the actual one 
    max_error=max(error_list)
    
    #plot the actual and the linear curve of the electrical characteristics in a specific input range
    plt.plot(physical,electrical,color='black', linewidth = 1,
             marker='o', markerfacecolor='black', markersize=3)
    plt.plot(physical, linear_function)
    plt.show()
    
    return error_list,max_error,slope   

def RubberRead():
    rubsensor.UpdateSensors()
    res = rubsensor.GetRes()
    return res

def accuracy(lenght,resistor_data_sheet,number_of_samples):
    """
    This function takes three inputs (lenght,resistor_data_sheet,number_of_samples) and return:
        1. res_measure:the actual measured value list 
        2. avg_resis: the average of measured values
        3. absolute_error= average measured value- resistor represented in the datasheet
    and plot the measured value with the true value to visualize the absolute error
    
    """
    res_measure=[None]*number_of_samples#to store the resistor measures
    abs_error=[None]*number_of_samples# to calculate the absolute error
    res_datasheet_list=[None]*number_of_samples
    avg_resis=[None]*number_of_samples
    t=[None]*number_of_samples
    sum_res=0#to calculate the average of the measured resistance
    for i in range(number_of_samples):
       t[i]=i
       res_measure[i]=RubberRead()
       res_datasheet_list[i]=resistor_data_sheet
       sum_res+=res_measure[i]
    avg_res=sum_res/number_of_samples
    for i in range(number_of_samples):
        avg_resis[i]=avg_res
        abs_error[i]=abs(avg_res-resistor_data_sheet)
    #plot the actual and the linear curve of the electrical characteristics in a specific input range
    
    plt.xlim([0, number_of_samples])
    plt.ylim([0, 2])
  
    plt.plot(t,res_measure,color='black', linewidth = 1,
             marker='o', markerfacecolor='black', markersize=3)
    plt.plot(t,res_datasheet_list,color='red')
    plt.plot(t,avg_resis,color='blue')
    plt.show()
    return res_measure,avg_resis,abs_error
#diff_1,hyst_1,max_index_1,avg_hysterisis_1 =hysterisis_calculation(printer_strain_t_1,printer_strain_c_1,resistor_t_1, resistor_c_1)
#linearity_error_list,linearity_error_1,sensitivity_12=linearity_error(printer_strain_t_linear_1,resistor_t_linear_1)
#non_linearity_error_list,non_linearity_error_1,sensitivity_1=non_linearity_error(printer_strain_t_1,resistor_t_1)
#res_measure_1,avg_resis_1,abs_error_1=accuracy(lenght_1,res_data_sheet_1,30)
res_measure_2,avg_resis_2,abs_error_2=accuracy(lenght_2,res_data_sheet_2,30)
