#### Basic Operation of Vector and Matrix

# Summary of NumPy Functions for Matrix Operations
"""
np.dot 
    Matrix multiplication (dot product) between two given arrays representing vectors, arrays, or tensors.
np.inner 
    Scalar multiplication (inner product) between two arrays representing vectors.
np.cross 
    The cross product between two arrays that represent vectors.
np.tensordot 
    Dot product along specified axes of multidimensional arrays.
np.outer 
    Outer product (tensor product of vectors) between two arrays representing vectors.
np.kron 
    Kronecker product (tensor product of matrices) between arrays representing matrices and higher-dimensional arrays.
np.einsum 
    Evaluates Einstein's summation convention for multidimensional arrays.
"""

#%%

import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
e = np.einsum("n,n",x,y)
e           # 70, e = x[1]*y[1] + x[2]*y[2] + x[3]*y[3] + ...

A = np.arange(0,6).reshape(2,3)
B = np.arange(0,6).reshape(3,2)
np.dot(A,B)
    # array([[10, 13],
    #        [28, 40]])
np.dot(B,A)
    # array([[ 3,  4,  5],
    #        [ 9, 14, 19],
    #        [15, 24, 33]])
B.dot(A)
    # array([[ 3,  4,  5],
    #        [ 9, 14, 19],
    #        [15, 24, 33]])

C = np.array([[1,2],
              [3,4]])
D = np.array([[9,8],
              [7,6]])
E = np.matrix(C)
    # matrix([[1, 2],
    #         [3, 4]])
F = np.matrix(D)
    # matrix([[9, 8],
    #         [7, 6]])
C*D
    # array([[ 9, 16],
    #        [21, 24]])
E*F
    # matrix([[23, 20],
    #         [55, 48]])
np.dot(C,D)
    # array([[23, 20],
    #        [55, 48]])

G = np.arange(0,4).reshape(1,4)
    # array([[0, 1, 2, 3]])
H = np.arange(0,4).reshape(4,1)
    # array([[0],
    #        [1],
    #        [2],
    #        [3]])
M = np.asmatrix(G)
    # matrix([[0, 1, 2, 3]])
N = np.asmatrix(H)
    # matrix([[0],
    #         [1],
    #         [2],
    #         [3]])
N.T
    # matrix([[0, 1, 2, 3]])
N.I
    # matrix([[0.        , 0.07142857, 0.14285714, 0.21428571]])
N.I*N
    # matrix([[1.]])
np.dot(G,H)
    # array([[14]])
np.dot(G,G.T)
    # array([[14]])
np.inner(G,G)
    # array([[14]])
np.inner(H,H)
    # array([[0, 0, 0, 0],
    #        [0, 1, 2, 3],
    #        [0, 2, 4, 6],
    #        [0, 3, 6, 9]])
np.outer(G,G)
    # array([[0, 0, 0, 0],
    #        [0, 1, 2, 3],
    #        [0, 2, 4, 6],
    #        [0, 3, 6, 9]])
np.outer(H,H)
    # array([[0, 0, 0, 0],
    #        [0, 1, 2, 3],
    #        [0, 2, 4, 6],
    #        [0, 3, 6, 9]])
# Kronecker product
P = np.arange(0,9).reshape(3,3)
Q = np.arange(1,5).reshape(2,2)
np.kron(M,N)
    # matrix([[0, 0, 0, 0],
    #         [0, 1, 2, 3],
    #         [0, 2, 4, 6],
    #         [0, 3, 6, 9]])
np.kron(N,M)
    # matrix([[0, 0, 0, 0],
    #         [0, 1, 2, 3],
    #         [0, 2, 4, 6],
    #         [0, 3, 6, 9]])

