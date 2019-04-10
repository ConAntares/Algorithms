#### Expand Determinant by the 1st Row

#%%
import numpy as np

# Input a n*n array as the determinant you want to analysis.
D = np.array([  [4,2,3],
                [3,4,6],
                [2,7,5] ])
# The number of row:
nRow = D.shape[1]
# The number of column:
nCol = D.shape[0]

# Initial sub determinant
Mvl = 

for n in np.arange(0,nCol):
    Mvl = D[1:nRow,:][:,0:n]
    Mvr = D[1:nRow,:][:,n+1:nCol]
    Mv = np.vstack((Mvl,Mvr))
    # Av = (-1)**(1+n)*Mv
    # print("The of remainder D[",n,"] is", Mv, ",")
    # print("The of algebraic remainder D[",n,"] is", Av, ".")