#### The Rank of Solution Space of Homogeneous Linear Equation Set

#%%
import numpy as np

# Input a array as the matrix you want to analysis.
D = np.array(   [[4,2,3,4],
                [3,4,5,5],
                [5,3,6,6],
                [3,3,9,6],
                [8,2,4,8],
                [2,4,9,5]]  )
# The rank of your matrix:
Rd = np.linalg.matrix_rank(D)
# The number of unknown numbers:
n = D.shape[1]
# The rank of solution space of homogeneous linear equation set
Rw = n - Rd

if Rd == n:
    print("The homogeneous linear equation set has zeros solutions." )
elif Rd < n:
    print("The homogeneous linear equation set has infinite solutions." )

print("The rank of solution space of homogeneous linear equation set is %s." %Rw )

