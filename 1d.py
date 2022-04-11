import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# forward time, mid-point position

t_steps = 500
pos_steps = 100
initial_condition = 2
grid = np.zeros((t_steps, pos_steps))
grid[0, pos_steps // 2 - 10:pos_steps // 2 + 10] = initial_condition
a = 0.05
dt = 0.1
dx = 1
F = a * dt / dx ** 2

for t in range(0, grid.shape[0] - 1):
    grid[t + 1, 1:-1] = grid[t, 1:-1] + a * (grid[t, 2:] - 2 * grid[t, 1:-1] + grid[t, :-2])

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, pos_steps), ylim=(0, initial_condition + 1))
ax.set_ylabel("T [a.u.]")
ax.set_xlabel("x [a.u.]")
line, = ax.plot([], [], lw=2, color="black")


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animation function.  This is called sequentially
def animate(i):
    x = range(len(grid[i, :]))
    y = grid[i, :]
    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=t_steps, interval=1)
anim.save('1d.gif')
plt.show()
