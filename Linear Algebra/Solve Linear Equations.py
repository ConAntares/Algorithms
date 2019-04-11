#### Solve Linear Equations

"""
In general, a linear equation system can be written on the form:
    A(m,n)*X(n*1)=B(m*1)
"""

import numpy as np

# Input a m*n array as the coefficient term matrix
A = np.array([[1,6,4,3],
              [6,2,1,9],
              [5,4,6,6],
              [4,5,2,5]])

# Input a m*1 array as the constant term matrix
B = np.array([[4],[3],[6],[1]])
# The augmented matrix
J = np.hstack((A,B))
# A zeros vector
Z = np.zeros((B.shape[0],1))
if B.any() == 0:
    print("The original equations set is homogeneous.")
elif B.any() != 0:
    print("The original equations set is not homogeneous.")

# The number of unknowns
n = A.shape[1]
# The rank of coefficient term matrix
Ra = np.linalg.matrix_rank(A)
# Calculate the value of determinant
Da = np.linalg.det(A)

if Da != 0:
    print("The original equations set has one solutions set.")
elif Da == 0:
    if Ra < n






    print("The original equations set has no solutions set or infinite solution sets.")