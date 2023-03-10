import serial as sr
import matplotlib.pyplot as plt
import numpy as np

s=sr.Serial('COM3',9600)
plt.close('all')
plt.figure()
plt.ion()
plt.show()
data1 = np.array([])
data2=np.array([])
i=0

while i<200000:
    a=s.readline()
    a.decode()
    print(a)
    resistor=float(a[0:4])
    #voltage=float(a[4:6])
    print(resistor)
    data1=np.append(data1,resistor)
    #data2=np.append(data2,voltage)
    plt.cla()
    plt.plot(data1)
    plt.pause(0.000001)
    i=i+1
s.close()