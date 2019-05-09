#### Elementary Vector

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

re = np.float64(A)
print(re)       # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

re = np.array([0,1,2,3,4,5,6,7,8,9],dtype=np.float64)
print(re)       # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

re = np.arange(0,10,2)
print(re)       # [0 2 4 6 8]

re = np.linspace(0,10,6)
print(re)       # [ 0.  2.  4.  6.  8. 10.]

re = np.zeros(10)
print(re)       # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

re = np.ones(10)
print(re)       # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

re = np.random.random(4)
print(re)       # [0.11097086 0.5790162  0.53776519 0.34051093]

A = np.array([1,2,3,4])
B = np.array([0,2,4,6])

re = A + 2
print(re)       # [3 4 5 6]

re = A * 2
print(re)       # [2 4 6 8]

re = A ** 2
print(re)       # [ 1  4  9 16]

re = A / 2
print(re)       # [0.5 1.  1.5 2. ]

re = A // 2
print(re)       # [0 1 1 2]

re = A % 2
print(re)       # [1 0 1 0]

re = A + B
print(re)       # [ 1  4  7 10]

re = A - B
print(re)       # [ 1  0 -1 -2]

re = A * B
print(re)       # [ 0  4 12 24]

re = A / B
print(re)       # [       inf 1.         0.75       0.66666667]

re = A // B
print(re)       # [0 1 0 0]

re = A % B
print(re)       # [0 0 3 4]

re = np.sum(A)
print(re)       # 10

A = np.matrix(A)
B = np.matrix(B)

re = np.dot(A,B.T)
print(re)       # [[40]]

re = np.dot(A.T,B)
print(re)
    # [[ 0  2  4  6]
    #  [ 0  4  8 12]
    #  [ 0  6 12 18]
    #  [ 0  8 16 24]]

