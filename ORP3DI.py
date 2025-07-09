import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def ORP3DI(centre):
    planets = ['Mercury','Venus','Earth','Mars','Jupiter']
    for i in range(len(planets)):
        if centre == planets[i]:
            cn = i
    # creating figure 
    fig = plt.figure()

    # setting up 3D plot
    ax = plt.axes(projection='3d')
    ax.set_xlim(-50, 50)
    ax.set_ylim(-40, 40)
    ax.set_zlim(-40, 40)
    ax.set_title("3D animation")

    # creating the moving points
    points = [ax.plot([], [], [], 'o', color='red')[0] for _ in range(4)]

    # eccentricity of planets
    e = [0.0565, 0.0457, 0.0113, 0.2488]

    # semi_major axis - 'a' in range equation
    a = [9.58, 19.29, 30.25, 39.51]

    # pi
    pi = 3.141592653589793238

    # beta values
    B = [7.00, 3.39, 0.00, 1.85, 1.31]

    x_list = [[],[],[],[]]
    y_list = [[],[],[],[]]
    z_list = [[],[],[],[]]

    # plot sun
    ax.scatter3D(0, 0, 0, color='yellow', s=100)

    # outer range for the 5 planets
    for i in range(4):
        B[i] = B[i] * (pi / 180)

        # nested for loop to calculate ellipse for each individual orbit
        for j in range(10000):
            theta = 0 + int(j) * ((2 * pi) / 10000)
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x = (x * math.cos(B[i]))
            z = (x * math.sin(B[i]))
            x_list[i].append(x)
            y_list[i].append(y)
            z_list[i].append(z)
        

    x_ani = [[], [], [], []]
    y_ani = [[], [], [], []]
    z_ani = [[], [], [], []]

    radians = [(2*pi / (0.24/ 11.86)),( 2*pi/ (0.62/ 11.86) ),( 2*pi/ (1.00 / 11.86) ),( 2*pi / (1.88/11.86) ),( 2*pi/ 1.00 )]

    for i in range(4):
        
        # nested for loop to calculate ellipse for each individual orbit
        for j in range(1000):
            theta = 0 + int(j) * ((radians[i]) / 1000)
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x = (x * math.cos(B[i]))
            z = (x * math.sin(B[i]))
            x_ani[i].append(x)
            y_ani[i].append(y)
            z_ani[i].append(z)

    for i in range(4):
        new_x = np.array(x_ani[cn]) - np.array(x_ani[i])
        new_y = np.array(y_ani[cn]) - np.array( y_ani[i])
        new_z = np.array(z_ani[cn]) - np.array( z_ani[i])
        plt.plot(new_x, new_y, new_z)
    plt.suptitle('3D')
plt.show()
