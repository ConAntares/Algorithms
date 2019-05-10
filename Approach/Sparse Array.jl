#### Sparse Array

using LinearAlgebra
using SparseArrays

n = 4
A = spzeros(n)
println(A)
    # 4-element SparseVector{Float64,Int64} with 0 stored entries

A = spzeros(Float64, 2,3)
println(A)
    # 2×3 SparseMatrixCSC{Float64,Int64} with 0 stored entries

A = sparse(I,2,3)
println(A)
    # 2×3 SparseMatrixCSC{Float64,Int64} with 0 stored entries
    #   [1, 1]  =  true
    #   [2, 2]  =  true

A = sparse(UniformScaling{Int}(10),3,4)
println(A)
    # [1, 1]  =  10
    # [2, 2]  =  10
    # [3, 3]  =  10

A = SparseMatrixCSC(I,3,4)
println(A)
    # [1, 1]  =  true
    # [2, 2]  =  true
    # [3, 3]  =  true

A = SparseMatrixCSC(UniformScaling{Int}(10),3,4)
println(A)
    # [1, 1]  =  10
    # [2, 2]  =  10
    # [3, 3]  =  10

A = SparseMatrixCSC(0.0*I,3,4)
println(A)
    # 3×4 SparseMatrixCSC{Float64,Int64} with 0 stored entries

A = SparseMatrixCSC(1.0*I,3,4)
println(A)
    # [1, 1]  =  1.0
    # [2, 2]  =  1.0
    # [3, 3]  =  1.0