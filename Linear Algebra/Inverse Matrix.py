#### Inverse Matrix.jl

import numpy as np

# Input a array as the matrix you want to analysis
S = np.array([[1,6,4,3],
              [6,2,1,9],
              [5,4,6,6],
            #   [4,5,2,5],
              [4,5,2,5]])
A = np.mat(S)

# The value of determinant
re = np.linalg.det(A)
print("The determinant value of this matrix is %f." %re)

if re == 0:
    print("This matrix is not invertible.")
else:
    print("This matrix is invertible.")
    im = np.linalg.inv(A)
    print("This inverse matrix is: \n",im)