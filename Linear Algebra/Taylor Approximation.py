#### Taylor Approximation

import math
import numpy as np

# About Taylor Approximation
"""
The first order Taylor Approximation of a function f: R^n → R, at the point z, is the affine function of x given by
fa(x) = f(z) + (∇f(z))'(x-z)
For x near z, fa(x) is very close to f(x).
"""

# A function and its Gradient
def f(x):
    return x[0] + math.exp(x[1] - x[0])

def grad_f(z):
    return [1 - math.exp(z[1] - z[0]), math.exp(z[1] - z[0])]

z = np.array([1, 2])

# The Taylor Approximation
def fa(x):
    return f(z) + np.dot(np.transpose(grad_f(z)), (x-z))

re = f([1,2])
print(re)       # 3.718281828459045
re = fa([1,2])
print(re)       # 3.718281828459045