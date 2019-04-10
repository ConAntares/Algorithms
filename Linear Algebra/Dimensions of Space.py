#### The Dimensions of Sub Space

#%%
import numpy as np

# Input 2 matrices as your spaces (only homogeneous linear equations analyzed):
S1 = np.array([1,2,-1])     # x + 2y -z = 0, z = x + 2y
S2 = np.array([2,1,-2])     # 2x + y -2z = 0, z  = x + 1/2y

# Intersection:
Si = np.intersect1d(S1, S2)

# The ranks of spaces:
R1 = np.linalg.matrix_rank(S1)
R2 = np.linalg.matrix_rank(S2)
Ri = np.linalg.matrix_rank(Si)

# The numbers of unknowns:
n1 = S1.shape[0]
n2 = S2.shape[0]
ni = Si.shape[0]

# The dimensions of solution spaces
D1 = n1 - R1
D2 = n2 - R2
Di = ni - Ri        # Intersection
Da = D1 + D2 - Di   # Sum

print("The dimension of solution space of your first equation set is",D1,",")
print("The dimension of solution space of your second equation set is",D2,",")
print("The dimension of solution space of the intersection is",Di,",")
print("The dimension of solution space of the sum is",Da,".")