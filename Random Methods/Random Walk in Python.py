#### Random Walk in Python

import numpy as np
import random as rd
import matplotlib as mpl
import matplotlib.pyplot as plt

def Walk(tot):
    x_values = [0]
    y_values = [0]

    while len(x_values) < tot:
        x_direction = rd.choice([-1,1])
        x_distance  = rd.choice([1,2,3,4])
        x_move      = x_direction * x_distance

        y_direction = rd.choice([-1,1])
        y_distance  = rd.choice([1,2,3,4])
        y_move      = y_direction * y_distance

        x_refresh   = x_values[-1] + x_move
        y_refresh   = y_values[-1] + y_move

        x_values.append(x_refresh)
        y_values.append(y_refresh)

    return x_values, y_values

re  = Walk(10000)
num = range(len(re[0]))

plt.rc("font", **{"size":14,"family":"serif","serif":["Computer Modern"]})
plt.rc("text", usetex = True)
fig, ax = plt.subplots(1,1)
plt.scatter(re[0], re[1], s=10, c=num)
plt.tick_params(direction='in')

plt.show()
