import numpy as np
import matplotlib.pyplot as plt
def K3L():
    # x values represent AU ( Distance form the sun )
    x = [0.387,0.723,1.000,1.523,5.20,9.58,19.29,30.25,39.51]

    #y values for orbital radius
    y = [0.24,0.62,1.00,1.88,11.86,29.63,84.75,166.34,248.35]

    # calculation the proprtinality of the semi major cubed
    semi_major_cubed = []
    for i in range(len(x)):
        value = x[i]**3
        new = value **(0.5)
        semi_major_cubed.append(new)




    # m is gradient and c is the y-intercept
    #m,c = np.polyfit(x,y,1)
    #m = int(m)

    # plot line of best fit
    print(semi_major_cubed)

    #labelling theh axis 

    plt.xlabel('AU')
    plt.ylabel('Orbital period')

    #plotting the graph
    plt.plot(semi_major_cubed,y)
    plt.scatter(semi_major_cubed,y, color="red")
    plt.suptitle('Kepler III')
    
plt.show()