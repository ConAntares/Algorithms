#### Vandermonde Matrix

# About
"""
An m×n Vandermonde matrix has enteries t(i,j-1) for i = 1,...,m and j = 1,...,n.
We define a function that takes an m-vector with elements t(1),...,t(m) and returns the corresponding m×n Vandermonde matrix.
"""

import numpy as np

def vandermonde(T,n):
    m = len(T)
    R = np.zeros((m,n))
    for i in range(0,m):
        for j in range(0,n):
            R [i,j] = T[i]**j
    return R

A = np.array([-1,0,0.5,1])
R = vandermonde(A,4)
print(R)
    # [[ 1.    -1.     1.    -1.   ]
    #  [ 1.     0.     0.     0.   ]
    #  [ 1.     0.5    0.25   0.125]
    #  [ 1.     1.     1.     1.   ]]