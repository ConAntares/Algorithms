#### Matrix Factorization

using LinearAlgebra

## Methods for Matrix Factorization/Decomposition
"""
Cholesky                Cholesky Factorization
CholeskyPivoted         Pivoted Cholesky Factorization
LU                      LU Factorization
LUTridiagonal           LU Factorization for Tridiagonal Matrix
UmfpackLU               LU Factorization for Tridiagonal Matrix
QR                      QR Factorization
QRCompactWY             Compact QR Factorization
Hessenberg              Hessenberg Factorization
Eigen                   Spectral Factorization
SVD                     SVD Factorization
GeneralizedSVD          General SVD Factorization
"""

A = [3.1 4.1;
     5.9 2.6]
B = [2.7 1.8;
     2.8 1.8]
E = [3.1 2.7;
     2.7 4.1]

re = cholesky(E)
println(re)
    # Cholesky{Float64,Array{Float64,2}}([1.76068 1.5335; 2.7 1.32227], 'U', 0)
println(re.U)
    # [1.76068 1.5335;
    #  0.0     1.32227]
println(re.L)
    # [1.76068 0.0;
    #  1.5335  1.32227]

Q,R = qr(A)
println(Q)
    # [-0.465128 -0.885243;
    #  -0.885243  0.465128]
println(R)
    # [-6.66483 -4.20866;
    #   0.0     -2.42017]

L,U,p = lu(A)
println(L)
    # [1.0      0.0; 
    #  0.525424 1.0]
println(U)
    # [5.9 2.6;
    #  0.0 2.7339]
println(p)
    # [2, 1]
re = A[p,:] - L*U
println(re)
    # [0.0 0.0; -4.44089e-16 0.0]