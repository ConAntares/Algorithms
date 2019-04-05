#### Basic Operation of Matrix

using LinearAlgebra
using SparseArrays

# Input some arrays as the matrics you want to analysis.
A = 
[
    1 2;
    3 4;
    5 6
]
B =
[
    3 2 1;
    4 3 2
]
C =
[
    4 1 2 3;
    2 3 4 1;
    1 2 3 4
]

## Matrix Multiplication

A*B
    # 3×3 Array{Int64,2}:
    #  11   8   5
    #  25  18  11
    #  39  28  17
B*A 
    # 2×2 Array{Int64,2}:
    #  14  20
    #  23  32
A*B*C
    # 3×4 Array{Int64,2}:
    #   65   45   69   61
    #  147  101  155  137
    #  229  157  241  213
A*(B*C)
    # 3×4 Array{Int64,2}:
    #   65   45   69   61
    #  147  101  155  137
    #  229  157  241  213
A*B*C == A*(B*C)
    # true

Va = [1 2 3]
Vb = [4;6;8]
Vb*Va
    # 3×3 Array{Int64,2}:
    #  4   8  12
    #  6  12  18
    #  8  16  24
J_3 = [1;1;1]*[1 1 1]
    # 3×3 Array{Int64,2}:
    #  1  1  1
    #  1  1  1
    #  1  1  1

A = 
[
    1 2 3 4
    2 3 4 5
    3 4 5 6
    4 5 6 7
]
A.^2
    # 4×4 Array{Int64,2}:
    #   1   4   9  16
    #   4   9  16  25
    #   9  16  25  36
    #  16  25  36  49
A^2
    # 4×4 Array{Int64,2}:
    #  30  40   50   60
    #  40  54   68   82
    #  50  68   86  104
    #  60  82  104  126
A^0
    # 4×4 Array{Int64,2}:
    #  1  0  0  0
    #  0  1  0  0
    #  0  0  1  0
    #  0  0  0  1

A = 
[
    1 2 3 4;
    4 1 2 3;
    3 4 1 2
]
B = 
[
    1 3 5 7;
    2 4 6 8;
    3 6 9 12
]
A'
    # 4×3 Adjoint{Int64,Array{Int64,2}}:
    #  1  4  3
    #  2  1  4
    #  3  2  1
    #  4  3  2

## Special Matrix

# Unit Matrix
I_3 = Array(UniformScaling{Float64}(1),3,3)
    # 3×3 Array{Float64,2}:
    #  1.0  0.0  0.0
    #  0.0  1.0  0.0
    #  0.0  0.0  1.0
I_3s = sparse(I,3,3)
    # 3×5 SparseMatrixCSC{Bool,Int64} with 3 stored entries:
    #   [1, 1]  =  true
    #   [2, 2]  =  true
    #   [3, 3]  =  true


A = 
[
    1 2 3;
    4 5 6;
    7 8 9
]

# Diagonal matrix
Diagonal(A)
    # 3×3 Diagonal{Int64,Array{Int64,1}}:
    #  1  ⋅  ⋅
    #  ⋅  5  ⋅
    #  ⋅  ⋅  9

# Diagonal matrix
UpperTriangular(A)
    # 3×3 UpperTriangular{Int64,Array{Int64,2}}:
    #  1  2  3
    #  ⋅  5  6
    #  ⋅  ⋅  9
LowerTriangular(A)
    # 3×3 LowerTriangular{Int64,Array{Int64,2}}:
    #  1  ⋅  ⋅
    #  4  5  ⋅
    #  7  8  9

# Fundamental matrix
A = zeros(3,3)
A[2,3] = 1
A
    # 3×3 Array{Float64,2}:
    #  0.0  0.0  0.0
    #  0.0  0.0  1.0
    #  0.0  0.0  0.0

# Elementary matrix
Ia = ones(4,4)
Is = Ia^0
Is[3,:]=4*Is[2,:]+Is[3,:]
Is
    # 4×4 Array{Float64,2}:
    #  1.0  0.0  0.0  0.0
    #  0.0  1.0  0.0  0.0
    #  0.0  4.0  1.0  0.0
    #  0.0  0.0  0.0  1.0
Ia = ones(4,4)
Is = Ia^0
Re=Is[3,:]
Is[3,:]=Is[2,:]
Is[2,:]=Re
Is
    # 4×4 Array{Float64,2}:
    #  1.0  0.0  0.0  0.0
    #  0.0  0.0  1.0  0.0
    #  0.0  1.0  0.0  0.0
    #  0.0  0.0  0.0  1.0