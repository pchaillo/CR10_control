import HG_C1100_P as ls
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time as t
lasensor = ls.SerialDuino()

# create figure and axe object
fig, ax = plt.subplots()

# set up the initial plot
time, distance = [], []
line, = ax.plot(time, distance)

# set the labels of the plot
plt.xlabel('Time (s)')
plt.ylabel('Distance (mm)')
plt.title('Distance versus Time')

# define a function that reads from the laser sensor
def laserRead():
    lasensor.UpdateSensors()
    dist = lasensor.Calcul_Strain()
    return dist

# define a function to update the plot
def update(i):
    # create a real-time distance read from the sensor
    dist = laserRead()
    time.append(0.29*i)
    distance.append(dist)

    # update the plot data
    line.set_xdata(time)
    line.set_ydata(distance)

    # set the axis limits
    ax.set_xlim(42, 100)
    ax.set_ylim(0, +100)

    # return the updated line object
    return line,

# create the animation object
# range is related to the time range,intervalle is related to delay

ani = animation.FuncAnimation(fig, update, frames=range(100000))

# show the plot
plt.show()
 

