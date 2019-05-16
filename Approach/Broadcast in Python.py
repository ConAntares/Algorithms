#### Broadcast

import numpy as np

A = np.array([[1,2],
              [3,4]])

B = np.array([10,20])

# Broadcast
r = A * B
print(r)
    # [[10 40]
    #  [30 80]]

# Matrix Multiplication
r = np.dot(A,B)
print(r)
    # [ 50 110]