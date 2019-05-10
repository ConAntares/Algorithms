#### Elementary Matrix

import numpy as np

A = np.array([[0.0, 0.1, 0.2, 0.3, 0.4],
              [1.8, 1.6, 1.4, 1.2, 1.0],
              [2.1, 2.3, 2.5, 2.7, 2.9]])

print(A.dtype)      # float64
print(A.size)       # 15
print(A.ndim)       # 2
print(A.shape)      # (3, 5)
