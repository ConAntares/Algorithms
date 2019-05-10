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
C = Matrix{Complex}([1.1 1.2 2.3;
                     3.4 5.5 8.6])
E = [3.14 1.59
     2.65 3.58]

println(typeof(A))  # Array{Float64,2}
println(typeof(B))  # Array{Float64,2}
println(typeof(C))  # Array{Complex,2}

re = A .+ 2
println(re)
     # [3.1 3.2  4.3;
     #  5.4 7.5 10.6]

re = A .- 2
println(re)
     # [-0.9 -0.8 0.3;
     #   1.4  3.5 6.6]

re = A .* 2
println(re)
     # [2.2  2.4  4.6;
     #  6.8 11.0 17.2]

re = A ./ 2
println(re)
     # [0.55 0.6  1.15;
     #  1.7  2.75 4.3]

re = A .% 2
println(re)
     # [1.1 1.2 0.3;
     #  1.4 1.5 0.6]

re = A .^ 2
println(re)
     # [ 1.21  1.44  5.29; 
     #  11.56 30.25 73.96]

re = A + B
println(re)
    # [4.2  5.3  8.2; 
    #  6.0 10.8 14.4]

re = A - B
println(re)
    # [-2.0 -2.9 -3.6;
    #   0.8  0.2  2.8]

re = A .* B
println(re)
    # [3.41  4.92 13.57; 
    #  8.84 29.15 49.88]

re = A ./ B
println(re)
    # [0.354839 0.292683 0.389831; 
    # 1.30769 1.03774 1.48276]

re = A' * B
println(re)
     # [12.25 22.53 26.21;
     #  18.02 34.07 38.98;
     #   29.49 55.01 63.45]

re = A * B'
println(re)
     # [21.9 22.56; 
     #  83.83 87.87]

re = tr(E)
println(re)
     # 6.720000000000001

re = rank(E)
println(re)
     # 2

re = det(E)
println(re)
     # 7.0277

re = eigvals(E)
println(re)
     # [1.29556, 5.42444]

re = eigvecs(E)
println(re)
     # [-0.652932 -0.571265; 0.757416 -0.820766]

A = [1.0 2.0;
      3.0 4.0]
B = [0.1 0.2;
      0.3 0.4]

re = A,B
println(re)
     # ([1.0 2.0; 3.0 4.0], 
     #  [0.1 0.2; 0.3 0.4])
println(typeof(re))
     # Tuple{Array{Float64,2},Array{Float64,2}}

re = (A,B)
println(re)
     # ([1.0 2.0; 3.0 4.0], 
     #  [0.1 0.2; 0.3 0.4])
println(typeof(re))
     # Tuple{Array{Float64,2},Array{Float64,2}}

re = [A B]
println(re)
     # [1.0 2.0 0.1 0.2;
     #  3.0 4.0 0.3 0.4]
println(typeof(re))
     # Array{Float64,2}

re = [A,B]
println(re)
     # [1.0 2.0 0.1 0.2;
     #  3.0 4.0 0.3 0.4]
println(typeof(re))
     # Array{Float64,2}

re = [A;B]
println(re)
     # [1.0 2.0 0.1 0.2;
     #  3.0 4.0 0.3 0.4]
println(typeof(re))
     # Array{Float64,2}

## Special Matrices
n = 4
A = Matrix{Float64}(I, n, n)
println(A)
    # [1.0 0.0 0.0 0.0; 
    #  0.0 1.0 0.0 0.0; 
    #  0.0 0.0 1.0 0.0; 
    #  0.0 0.0 0.0 1.0]

A = zeros(Float64,n,n)
println(A)
    # [0.0 0.0 0.0 0.0; 
    #  0.0 0.0 0.0 0.0; 
    #  0.0 0.0 0.0 0.0; 
    #  0.0 0.0 0.0 0.0]

A = ones(Float64,n,n)
println(A)
    # [1.0 1.0 1.0 1.0; 
    #  1.0 1.0 1.0 1.0; 
    #  1.0 1.0 1.0 1.0;
    #  1.0 1.0 1.0 1.0]

A = trues(n,n)
println(A)
     # Bool[true true true true;
     #      true true true true; 
     #      true true true true;
     #      true true true true]

A = falses(n,n)
println(A)
     # Bool[false false false false;
     #      false false false false;
     #      false false false false;
     #      false false false false]
