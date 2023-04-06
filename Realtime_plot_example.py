import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

# set up the initial plot
x, y = [], []
line, = ax.plot(x, y)

# define a function to update the plot
def update(i):
    # generate a random data point
    x.append(i)
    y.append(random.randint(0, 10))

    # update the plot data
    line.set_xdata(x)
    line.set_ydata(y)

    # set the axis limits
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(0, 10)

    # return the updated line object
    return line,

# create the animation object
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=5000)
# range is related to the time,intervalle is related to delay
# show the plot
plt.show()
