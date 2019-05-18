#### Adjoint Matrix

using LinearAlgebra

# Input a array as the matrix you want to analysis
A = [1 6 4 3;
     6 2 1 9;
     5 4 6 6;
     4 5 2 4;]

# The value of determinant
det(A)
# The rank
rank(A)
# The inverse matrix
inv(A)
# The transposed matrix
A'
# The conjugate matrix
conj(A)
# The adjoint matrix
det(A)*inv(A)