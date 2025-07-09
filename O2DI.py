import numpy as np
import matplotlib.pyplot as plt
import math
def O2DI():
    #eccentricity of planets
    e = [0.2056, 0.0067, 0.0167, 0.0934, 0.0484]
    #semi_major axis - 'a' in range equation
    a = [0.387,0.723,1.000,1.523,5.20,9.58,19.29,30.25,39.51]
    pi = 3.141592653589793238

    x_list = []
    y_list = []

    # plot sun

    plt.scatter(0, 0, color='yellow', s = 100)

    #outer range for the 5 planets
    for i in range(5):
        if len(x_list) > 0:
            x_list.clear()
            y_list.clear()
        #nested for loop to calculate elipse for each individual orbit
        for j in range(1000):
            theta = 0 + int(j)*((2*pi)/1000) #starting at theta = 0 incrementing by 2 pi / 1000 each time to form the elipse
            r = a[i]*(1- (e[i]**2)) / (1 - e[i]* math.cos(theta))
            x = (r* math.cos(theta))
            y = (r* math.sin(theta))
            x_list.append(x)
            y_list.append(y)
            
        plt.plot(x_list, y_list)
    plt.suptitle('2D First 5 Planets')
plt.show()