import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
def O2DAO():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-50,50)
    ax.set_ylim(-40,40)

    # Create empty point objects for each orbit
    points = [ax.plot([], [], 'o', color='red')[0] for i in range(4)]

    # Eccentricity of planets
    e = [0.0565, 0.0457, 0.0113, 0.2488]
    # Semi-major axis - 'a' in range equation
    a = [9.58, 19.29, 30.25, 39.51]
    pi = 3.141592653589793238

    #these are the arrays that contain the x and y co-ordinates for the lines
    x_list = [[], [], [], []]
    y_list = [[], [], [], []]

    #these are the x and y co-ordinates to plot the animation pointa
    x_ani = [[],[],[],[]]
    y_ani = [[],[],[],[]]

    # to calcualte the co-ordiantes of the line 
    for i in range(4):
        for j in range(1000):
            theta = 0 + int(j) * ((2 * pi) / 1000)  # Starting at theta = 0 incrementing by 2 pi / 1000 each time to form the ellipse
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x_list[i].append(x)
            y_list[i].append(y)
        ax.plot(x_list[i], y_list[i])

    # to calcualte the theta values for the planets

        radians = [( 2*pi/ (29.63/  248.35) ),( 2*pi/ (84.75 /  248.35) ),( 2*pi / (166.34/ 248.35) ),( 2*pi/ 1.00)]
        #radians = [ 2*pi/ (29.63), (2*pi/ 84.75) ,( 2*pi / 166.34),( 2*pi/ 248.35)]


    # to calcualte the co-ordiantes of the moving pointa 

    for i in range(4):
        for j in range(200):
            theta = 0 + int(j) * (radians[i] / 200)  # Starting at theta = 0 incrementing by 2 pi / 1000 each time to form the ellipse
            r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
            x = (r * math.cos(theta))
            y = (r * math.sin(theta))
            x_ani[i].append(x)
            y_ani[i].append(y)

    # Animation function
    def update(frame):
        # years
        x = str(frame)
        print(frame)
        #fig,ax.set_title('Years = ' + x)
        # Update the position of each point on each orbit
        for i in range(4):                
            x = x_ani[i][frame]
            y = y_ani[i][frame]
            # Update the position of the point
            points[i].set_data([x], [y])

        return points

    # Create the animation
    animation = FuncAnimation(fig, update, blit=True, frames = 200)

# Display the animation
    #plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode
    plt.show()
