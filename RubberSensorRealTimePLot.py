import matplotlib.pyplot as plt
import matplotlib.animation as animation
import RubberSensor as rs

rubsensor=rs.RubberSerialDuino()
# create figure and axe object
fig, ax = plt.subplots()

# set up the initial plot
time, resistance= [], []
line, = ax.plot(time, resistance)

# set the labels of the plot
plt.xlabel('Time (s)')
plt.ylabel('resistance (ohm)')
plt.title('resistance versus Time')

# define a function that reads from the rubber sensor
def RubberRead():
    rubsensor.UpdateSensors()
    res = rubsensor.GetRes()
    return res

# define a function to update the plot
def update(i):
    # create a real-time distance read from the sensor
    res = RubberRead()
    time.append(i)
    resistance.append(res)

    # update the plot data
    line.set_xdata(time)
    line.set_ydata(resistance)

    # set the axis limits
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(1, 2)

    # return the updated line object
    return line,

# create the animation object
# range is related to the time range,intervalle is related to delay
ani = animation.FuncAnimation(fig, update, frames=range(1000000))

# show the plot
plt.show()
 

