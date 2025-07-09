import numpy as np
import matplotlib.pyplot as plt
import math

def OAT(planet):
    
    def theta(t, P, ecc):
        N = round(t / P)  # Number of orbits
        theta_steps = 1000
        
        theta_list = np.linspace(0, 2 * np.pi * N, theta_steps)
        f_list = (1 - ecc * np.cos(theta_list))**(-2)
        
        c_list = [1] + [4 if i % 2 == 0 else 2 for i in range(theta_steps - 2)] + [1]
        
        b = theta_list[-1]
        tt = P * (1 - ecc**2)**(1.5) * (1 / (2 * np.pi)) * b * (1 / theta_steps) * (1 / 3) * np.cumsum(np.array(c_list) * f_list)
        
        return tt, theta_list

    # Define planet data
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    ecc = [0.2056, 0.0067, 0.0167, 0.0934, 0.0484, 0.0565, 0.0457, 0.0113, 0.2488]
    orbit_time = [0.24, 0.62, 1, 1.88, 11.86, 29.63, 84.75, 166.34, 248.35]
    
    for i in range(len(planets)):
        if planet == planets[i]:
            e = ecc[i]
            p = orbit_time[i]
           
    x, y = theta(3 * p, p, e)  # Plot for 3 periods
    plt.plot(x, y)
    plt.suptitle('Orbit Angle Vs Time')
    plt.xlabel('Time')
    plt.ylabel('Orbit Angle')
    x_coords = [x[0], x[-1]]
    y_coords = [y[0], y[-1]]
    plt.plot(x_coords, y_coords, linestyle='-', color='r', label='Line')

plt.show()



