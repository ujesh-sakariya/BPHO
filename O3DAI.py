import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
def O3DAI():
    # creating figure 
    fig = plt.figure()

    # setting up 3D plot
    ax = plt.axes(projection='3d')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-0.5, 0.5)
    ax.set_title("3D animation")

    # creating the moving points
    points = [ax.plot([], [], [], 'o', color='red')[0] for _ in range(5)]

    # eccentricity of planets
    e = [0.2056, 0.0067, 0.0167, 0.0934, 0.0484]

    # semi_major axis - 'a' in range equation
    a = [0.387, 0.723, 1.000, 1.523, 5.20, 9.58, 19.29, 30.25, 39.51]

    # pi
    pi = 3.141592653589793238

    # beta values
    B = [7.00, 3.39, 0.00, 1.85, 1.31]

    x_list = []
    y_list = []
    z_list = []

    # plot sun
    ax.scatter3D(0, 0, 0, color='yellow', s=100)

    # outer range for the 5 planets
    for i in range(5):
        B[i] = B[i] * (pi / 180)
        if len(x_list) > 0:
            x_list.clear()
            y_list.clear()
            z_list.clear()
        # nested for loop to calculate ellipse for each individual orbit
        for j in range(1000):
            theta = 0 + int(j) * ((2 * pi) / 1000)
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x = (x * math.cos(B[i]))
            z = (x * math.sin(B[i]))
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
        ax.plot(x_list, y_list, z_list)

    x_ani = [[], [], [], [], []]
    y_ani = [[], [], [], [], []]
    z_ani = [[], [], [], [], []]

    radians = [(2*pi / (0.24/ 11.86)),( 2*pi/ (0.62/ 11.86) ),( 2*pi/ (1.00 / 11.86) ),( 2*pi / (1.88/11.86) ),( 2*pi/ 1.00 )]

    for i in range(5):
        if len(x_list) > 0:
            x_list.clear()
            y_list.clear()
            z_list.clear()
        # nested for loop to calculate ellipse for each individual orbit
        for j in range(200):
            theta = 0 + int(j) * ((radians[i]) / 200)
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x = (x * math.cos(B[i]))
            z = (x * math.sin(B[i]))
            x_ani[i].append(x)
            y_ani[i].append(y)
            z_ani[i].append(z)

    def update(frame):
        for i in range(5):
            x = x_ani[i][frame]
            y = y_ani[i][frame]
            z = z_ani[i][frame]
            points[i].set_data([x], [y])
            points[i].set_3d_properties([z])
        return points

    # Create the animation
    animation = FuncAnimation(fig, update, blit=True, frames=200)
    ax.dist = 7
    #plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode 
    plt.show()

