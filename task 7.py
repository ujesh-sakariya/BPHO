import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Set up the figure and axis
fig, ax = plt.subplots()


# earth
plt.scatter(0, 0, color='blue', s = 100)
# Create empty point objects for each orbit


# Eccentricity of planets
e = [0.2056, 0.0067, 0.0167, 0.0934, 0.0484]
# Semi-major axis - 'a' in range equation
a = [0.387, 0.723, 1.000, 1.523, 5.20, 9.58, 19.29, 30.25, 39.51]
pi = 3.141592653589793238

#these are the arrays that contain the x and y co-ordinates for the lines
x_list = [[], [], [], [], []]
y_list = [[], [], [], [], []]

#these are the x and y co-ordinates to plot the animation pointa
x_ani = [[],[],[],[],[]]
y_ani = [[],[],[],[],[]]

# to calcualte the co-ordiantes of the line 
for i in range(5):
    for j in range(100000):
        theta = 0 + int(j) * ((6 * pi) / 100000)  # Starting at theta = 0 incrementing by 2 pi / 1000 each time to form the ellipse
        r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
        x = (r * math.cos(theta))
        y = (r * math.sin(theta))
        x_list[i].append(x)
        y_list[i].append(y)
    
# to calcualte the theta values for the planets

    radians = [(45*pi / (0.24/ 11.86)),(40*pi/ (0.62/ 11.86) ),( 2*pi/ (1.00 / 11.86) ),(40*pi / (1.88/11.86) ),(40*pi/ 1.00 )]

# to calcualte the co-ordiantes of the moving pointa 

for i in range(5):
    for j inrange(500)::
        theta = 0 + int(j) * (radians[i] /5000)  # Starting at theta = 0 incrementing by 2 pi / 1000 each time to form the ellipse
        r = a[i] * (1 - (e[i] ** 2)) / (1 - e[i] * math.cos(theta))
        x = (r * math.cos(theta))
        y = (r * math.sin(theta))
        x_ani[i].append(x)
        y_ani[i].append(y)

for i in range(4):
    new_x = np.array(x_ani[0]) - np.array(x_ani[i])
    new_y = np.array(y_ani[0]) - np.array( y_ani[i])
    plt.plot(new_x, new_y)
plt.show()
