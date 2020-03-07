#### #### Matrix Elimination and LU Decomposition

import numpy as np
from scipy.linalg import lu

# Input a n*n array as the determinant you want to analysis.
D = np.array([[4,1,5,4,3],
              [3,4,6,2,5],
              [2,7,5,1,3],
              [1,6,4,3,6],
              [2,1,6,5,4]])

# LU Decomposition
pl, U = lu(D, permute_l=True)
print(U)
    # [[ 4.          1.          5.          4.          3.        ]
    #  [ 0.          6.5         2.5        -1.          1.5       ]
    #  [ 0.          0.          3.30769231  3.07692308  2.38461538]
    #  [ 0.          0.          0.          2.38372093  3.53488372]
    #  [ 0.          0.          0.          0.          3.4       ]]
