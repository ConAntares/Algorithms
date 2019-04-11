#### Expand Determinant by the 1st Row

import numpy as np

# Input a n*n array as the determinant you want to analysis.
D = np.array([  [4,2,3],
                [3,4,6],
                [2,7,5] ])
# The number of row:
nRow = D.shape[1]
# The number of column:
nCol = D.shape[0]

for n in np.arange(0,nCol):
    Mvl = D[1:nRow,:][:,0:n]
    Mvr = D[1:nRow,:][:,n+1:nCol]
    Mv = np.hstack((Mvl,Mvr))
    Av = (-1)**(1+n-1)*Mv
    print("The of remainder D[(%s)] is \n" %n, Mv)   
    print("The of algebraic remainder D[(%s)] is \n" %n, Av)