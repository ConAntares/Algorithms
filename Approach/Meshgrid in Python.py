#### Meshgrid

import numpy as np

u = np.array([0.0, 0.1, 0.2])
b = np.array([1.0, 1.1, 1.2])
U,B = np.meshgrid(u,b)

print(U)
    # [[0.  0.1 0.2]
    #  [0.  0.1 0.2]
    #  [0.  0.1 0.2]]
print(B)
    # [[1.  1.  1. ]
    #  [1.1 1.1 1.1]
    #  [1.2 1.2 1.2]]