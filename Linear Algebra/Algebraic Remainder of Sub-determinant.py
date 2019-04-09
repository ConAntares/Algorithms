#### Algebraic Remainder of Sub-determinant

#%%
import numpy as np

# Input a n*n array as the determinant you want to analysis.
D = np.array([  [4,1,5,4,3],
                [3,4,6,2,5],
                [2,7,5,1,3],
                [1,6,4,3,6],
                [2,1,6,5,4] ])
n = D.shape[0]

# The number of sub-determinant's ordinal:
k = 3
# Input the ordinals of rows you want to extract:
I = np.array([0,2,4])
# Input the ordinals of columns you want to extract:
J = np.array([1,2,3])

S = D[:,J][I,:]
S   # Sub-determinant
    # array([[1, 5, 4],
    #        [7, 5, 1],
    #        [1, 6, 5]])
N = np.arange(0,n,1)
Im = np.array(list(set(N).difference(set(I))))
Jm = np.array(list(set(N).difference(set(J))))
M = D[:,Jm][Im,:]
M   # The remainder
    # array([[3, 5],
    #        [1, 6]])
A = (-1)**(sum(I)+sum(J))*M
A   # The algebraic remainder
    # array([[3, 5],
    #        [1, 6]])


