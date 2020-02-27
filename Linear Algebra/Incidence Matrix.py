#### Incidence Matrix

import numpy as np

A = np.array([[-1,-1, 0, 1, 0],
              [ 1, 0,-1, 0, 0],
              [ 0, 0, 1,-1,-1],
              [ 0, 1, 0, 0, 1]])

xCirc = (np.array([1,-1, 1, 0, 1]) ).T

Re = np.dot(A,xCirc)
print(Re)       # [0 0 0 0]