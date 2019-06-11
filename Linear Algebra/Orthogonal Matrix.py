#### Orthogonal matrix

import numpy as np

# Input a n*n array as the matrix you want to analysis.
S = np.array([[1,0,0],
              [0,0,1],
              [0,1,0]])
D = np.mat(S)

# The value of determinant
re = np.linalg.det(D)
print("The determinant value of this matrix is %f." %re)

if re == 0:
    print("This matrix is not invertible.")
else:
    print("This matrix is invertible.")
    Im = np.linalg.inv(D)
    Tm = np.transpose(D)
    if (Im == Tm).all():
        print("This matrix is orthogonal.")
    else:
        print("This matrix is not orthogonal.")
