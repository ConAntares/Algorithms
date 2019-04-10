#### Rank of Matrix

#%%
import numpy as np

# Input a n*n array as the matrix you want to analysis.
D = np.array([  [4,2,3],
                [3,4,6],
                [5,3,1] ])
# Then the Rd is the rank of your matrix:
Rd = np.linalg.matrix_rank(D)
print("The rank of your matrix is",Rd)

# Input a 1*n array as the vector of constant term.
C = np.array([[1],[2],[3]])
# The augmented matrix is:
A = np.hstack((D,C))
# The rank of the augmented:
Ra = np.linalg.matrix_rank(A)
print("The rank of your augmented matrix is",Ra)

if Rd == Ra:
    if Rd == D.shape[1]:
        print("The equation set which determined by matrix A has a solution.")
    elif Rd < D.shape[1]:
        print("The equation set which determined by matrix A has infinite solutions.")
elif Rd < Ra:
    print("The equation set which determined by matrix A has no solution.")
