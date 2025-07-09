import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

def S(planet1,planet2):

    planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
    ecc = [0.2056, 0.0067, 0.0167, 0.0934, 0.0484, 0.0565, 0.0457, 0.0113, 0.2488]
    a = [0.387, 0.723, 1.000, 1.523, 5.20, 9.58, 19.29, 30.25, 39.51]
    for i in range(len(planets)):
        if planets[i] == planet1:
            ecc1 = ecc[i]
            ax1 = a[i]

    for i in range(len(planets)):
        if planets[i] == planet2:
            ecc2 = ecc[i]
            ax2 = a[i]

    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Eccentricity of planets
    e = [ecc1,ecc2]
    # Semi-major axis - 'a' in range equation
    a = [ax1,ax2]
    pi = 3.141592653589793238

    # Calculate the theta values for the planets
    radians = [(2 * pi / (0.62 / 11.86)), (2 * pi / (1.00 / 11.86))]

    # Calculate the coordinates of the moving points
    x_ani = [[], []]
    y_ani = [[], []]
    for i in range(2):
        for j in range(500):
            theta = 0 + int(j) * (radians[i] / 500)
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x_ani[i].append(x)
            y_ani[i].append(y)

    # Create point objects for the moving points on each orbit
    points = [ax.plot([], [], 'o', color='red')[0] for i in range(2)]

    # Create line objects for the lines connecting the moving points
    lines = [ax.plot([], [], linestyle='-', color='grey', linewidth=0.5)[0] for _ in range(500)]

    # Animation function
    def update(frame):
        # years
        #ax.set_title('Years = ' + str(frame))
        # Update the position of each point on each orbit

        x_list = [x_ani[i][frame] for i in range(2)]
        y_list = [y_ani[i][frame] for i in range(2)]

        # Update the position of the points
        points[0].set_data([x_list[0]], [y_list[0]])
        points[1].set_data([x_list[1]], [y_list[1]])

        # Plot the spirograph line for the current frame
        lines[frame].set_data([x_list[0], x_list[1]], [y_list[0], y_list[1]])

        return points + lines

    # Create the animation
    animation = FuncAnimation(fig, update, blit=True, frames=500)

    # Plot the orbits without lines between them using different colors
    orbit1, = ax.plot(x_ani[0], y_ani[0], color='green', linestyle='-')
    orbit2, = ax.plot(x_ani[1], y_ani[1], color='blue', linestyle='-')

    # Display the animation
    #plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode
    plt.show()

