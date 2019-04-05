#### Array in Julia

# Input a n*m array as the matrix you want to analysis.
A = 
[
    4 2 3 5;
    3 4 6 2;
    5 3 1 4;
]

# Type of elements in array:
eltype(A)       # Int64

# number of elements in array:
length(A)       # 12

# Dimensions of elements in array:
ndims(A)        # 2

# Size of array:
size(A)         # (3, 4)

# Size of array in dimension 1:
size(A,1)       # 3

# Size of array in dimension 2:
size(A,2)       # 4

# The initial array:
S = Array{Float64}(undef,2,3)
    # 2×3 Array{Float64,2}:
    #  0.0  0.0  0.0
    #  0.0  0.0  0.0