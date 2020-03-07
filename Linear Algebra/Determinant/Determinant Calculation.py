#### Determinant Calculation

import numpy as np

# Input a n*n array as the determinant you want to calculate.

A = np.array([  [4,2,3,5],
                [3,4,6,3],
                [2,7,5,4],
                [5,3,4,3]   ])

# Calculate the value of determinant
np.linalg.det(A)    # 186.9999999999999
# Calculate the value of transposed determinant
np.linalg.det(A.T)  # 186.9999999999999