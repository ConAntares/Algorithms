#### Elementary Array

import numpy as np

A = np.array([0,1,2,3,4,5,6,7,8,9])
print(A)        # [0 1 2 3 4 5 6 7 8 9]
print(A[1])     # 1
print(A[1:5])   # [1 2 3 4]
print(A[5:1])   # []
print(len(A))   # 10
print(type(A))  # <class 'numpy.ndarray'>
print(A.dtype)  # int32
print(A.ndim)   # 1
print(A.shape)  # (10,)
print(A.nbytes) # 40

B = np.float64(A)
print(B)        # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

C = np.array([0,1,2,3,4,5,6,7,8,9],dtype=np.float64)
print(C)        # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

D = np.arange(0,10,2)
print(D)        # [0 2 4 6 8]

E = np.linspace(0,10,6)
print(E)        # [ 0.  2.  4.  6.  8. 10.]