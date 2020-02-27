#### Dirichlet Energy

import numpy as np

A = np.array([[-1,-1, 0, 1, 0],
              [ 1, 0,-1, 0, 0],
              [ 0, 0, 1,-1,-1],
              [ 0, 1, 0, 0, 1]])

VSmooth = np.array([1, 2, 2, 1])
VRough  = np.array([1,-1, 2,-1])

nSmooth = np.linalg.norm(np.dot(A.T,VSmooth))**2
nRough  = np.linalg.norm(np.dot(A.T,VRough))**2

print(nSmooth,"\n",nRough)
    # 2.9999999999999996 
    # 27.0