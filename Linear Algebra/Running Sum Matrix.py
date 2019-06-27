### Running Sum Matrix

# About Running Sum Matrix
"""
R = [ 1 0 0 0;
      1 1 0 0;
      1 1 1 0;
      1 1 1 1 ]
X = [ a b c d ]
R*X = [ a a+b a+b+c a+b+c+d]
"""

import numpy as np

def running_sum(n):
    return np.tri(n,n)

A = running_sum(4)
print(A)
    # [[1. 0. 0. 0.]
    #  [1. 1. 0. 0.]
    #  [1. 1. 1. 0.]
    #  [1. 1. 1. 1.]]