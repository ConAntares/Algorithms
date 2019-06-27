#### Vandermonde Matrix

# About
"""
An m×n Vandermonde matrix has enteries t(i,j-1) for i = 1,...,m and j = 1,...,n.
We define a function that takes an m-vector with elements t(1),...,t(m) and returns the corresponding m×n Vandermonde matrix.
"""

function vandermonde(T,n)
    m = length(T)
    R = zeros(m,n)
    for i = 1:m
        for j = 1:n
            R[i,j] = T[i]^(j-1)
        end
    end
    return R
end

A = [-1,0,0.5,1]
R = vandermonde(A,4)
    # 4×4 Array{Float64,2}:
    #  1.0  -1.0  1.0   -1.0
    #  1.0   0.0  0.0    0.0
    #  1.0   0.5  0.25   0.125
    #  1.0   1.0  1.0    1.0
