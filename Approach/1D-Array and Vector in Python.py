#### Elementary Vector

import numpy as np

## Summary of NumPy functions for generating arrays
"""
np.array:
    Creates an array for which the elements are given by an array-like object, which,
    for example, can be a (nested) Python list, a tuple, an iterable sequence,
    or another ndarray instance.
np.zero:
    Creates an array – with the specified dimensions and data type – that is filled with zeros.
np.ones:
    Creates an array – with the specified dimensions and data type – that is filled with ones.
np.diag:
    Creates an array with evenly spaced values between specified start, end, and, increment values.
np.linspace:
    Creates an array with evenly spaced values between specified start and end values,
    using a specified number of elements.
np.logspace:
    Creates an array with values that are logarithmically spaced between the given start and end values.
np.meshgrid:
    Generate coordinate matrices (and higher-dimensional coordinate arrays) from onedimensional coordinate vectors.
np.fromfunction:
    Create an array and fill it with values specified by a given function,
    which is evaluated for each combination of indices for the given array size.
np.fromfile:
    Create an array with the data from a binary (or text) file.
    NumPy also provides a corresponding function np.tofile with which NumPy arrays can be stored to disk,
    and later read back using np.fromfile.
np.loadtxt, np.genfromtxt:
    Creates an array from data read from a text file. For example, a comma-separated value. (CSV) file.
    The function np.genfromtxt also supports data files with missing values.
np.random.rand:
    Generates an array with random numbers that are uniformly distributed between 0 and 1.
    Other types of distributions are also available in the np.random module.
"""

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

re = np.empty(10)
print(re)       # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

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

re = np.sqrt(A)
print(re)       # [1.         1.41421356 1.73205081 2.        ]

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

## Special Array

n = 4
re = np.empty(n, dtype=np.float64)
print(re)
    # [5.e-324 4.e-323 4.e-323 4.e-323]

re = np.zeros(n)
print(re)
    # [0. 0. 0. 0.]

re = np.ones(n)
print(re)
    # [1. 1. 1. 1.]
