#### Random Walk in Python

import numpy as np
import random as rd
import matplotlib as plt

def Walk(tot):
    x_values = [0]
    y_values = [0]

    while len(x_values) < tot:
        x_direction = rd.choice([-1,1])
        x_distance  = rd.choice([1,2,3,4])
        x_move      = x_direction * x_distance

        y_direction = rd.choice([-1,1])
        y_distance  = rd.choice([1,2,3,4])
        y_move      = x_direction * x_distance

