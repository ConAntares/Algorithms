#### Trace

import numpy as np

# Input a array as the matrix you want to analysis
S = np.array([[1,6,4,3],
              [6,2,1,9],
              [5,4,6,6],
              [4,5,2,5]])
A = np.mat(S)

tr = sum(A[n,n] for n in range(0,len(A)))
print("The trace of this matrix is %f." %tr)