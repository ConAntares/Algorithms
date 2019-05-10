#### Elementary Matrix

using LinearAlgebra

A = 
[
    0.0 0.1 0.2 0.3 0.4;
    1.8 1.6 1.4 1.2 1.0;
    2.1 2.3 2.5 2.7 2.9;
]

println(eltype(A))      # Float64
println(length(A))      # 15
println(ndims(A))       # 2
println(size(A))        # (3,5)
println(size(A,1))      # 3
println(size(A,2))      # 5

A = [1.1 1.2 2.3;
     3.4 5.5 8.6]
B = [3.1 4.1 5.9;
     2.6 5.3 5.8]

# re = A + B
# println(re)
#     # [4.2  5.3  8.2; 
#     #  6.0 10.8 14.4]
# re = A - B
# println(re)
#     # [-2.0 -2.9 -3.6;
#     #   0.8  0.2  2.8]
# re = A .* B
# println(re)
#     # [3.41  4.92 13.57; 
#     #  8.84 29.15 49.88]
# re = A ./ B
# println(re)
#     # [0.354839 0.292683 0.389831; 
#     # 1.30769 1.03774 1.48276]


# ## Special Matrices
# n = 4
# A = Matrix{Float64}(I, n, n)
# println(A)
#     # [1.0 0.0 0.0 0.0; 
#     #  0.0 1.0 0.0 0.0; 
#     #  0.0 0.0 1.0 0.0; 
#     #  0.0 0.0 0.0 1.0]

# A = zeros(Float64,n,n)
# println(A)
#     # [0.0 0.0 0.0 0.0; 
#     #  0.0 0.0 0.0 0.0; 
#     #  0.0 0.0 0.0 0.0; 
#     #  0.0 0.0 0.0 0.0]

# A = ones(Float64,n,n)
# println(A)
#     # [1.0 1.0 1.0 1.0; 
#     #  1.0 1.0 1.0 1.0; 
#     #  1.0 1.0 1.0 1.0;
#     #  1.0 1.0 1.0 1.0]