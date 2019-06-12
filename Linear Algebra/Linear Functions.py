#### Linear Functions

import numpy as np

## Functions in Python
def f1(X):
    return X[0] + X[1] - X[3]**2

re = f1(np.array([-1,0,1,2]))
print(re)         # -5

## Superposition
# Inner Product Function
A = np.array([-2,0,1,-3])
def f2(X):
    return np.dot(np.transpose(A), X)

re = f2(np.array([-1,0,1,2]))
print(re)         # -3
