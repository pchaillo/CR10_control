import HG_C1100_P as ls
import matplotlib.pyplot as plt
import time
LaserSensor=ls.SerialDuino()
n_samples=1000000
i=0
plt.ylabel('distance')
plt.title('distance versus time')

while i<= n_samples:
 
 LaserSensor.UpdateSensors()
 dist=LaserSensor.GetDist()
 print(dist)
 plt.plot(dist)
 plt.show()
 i+=1
