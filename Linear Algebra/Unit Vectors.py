#### Unit Vectors

import numpy as np

def unit_vector(i,n):
    return np.hstack((np.zeros(i-0), 1, np.zeros(n-i-1)))

print(unit_vector(1,4))   # [0. 1. 0. 0.]