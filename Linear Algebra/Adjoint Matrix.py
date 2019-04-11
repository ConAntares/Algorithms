#### Adjoint Matrix

import numpy as np

# Input a array as the matrix you want to analysis
S = np.array([[1,6,4,3],
              [6,2,1,9],
              [5,4,6,6],
              [4,5,2,5]])
A = np.mat(S)

# The value of determinant
np.linalg.det(A)
# The rank
np.linalg.matrix_rank(A)
# The inverse matrix
np.linalg.inv(A)
# The transposed matrix
A.T
# The conjugate transpose matrix
A.H
# The adjoint matrix
print(np.linalg.det(A)*np.linalg.inv(A))