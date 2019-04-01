#### Rank of Matrix

using LinearAlgebra

# Input a n*n array as the matrix you want to analysis.
D = 
[
    4 2 3;
    3 4 6;
    2 7 5;
]
# Then the Rd is the rank of your matrix:
Rd = rank(D)
println("The rank of your matrix is $Rd")

# Input a 1*n array as the vector of constant term.
C = [1,2,3]
# The augmented matrix is:
A = [D C]
# The rank of the augmented:
Ra = rank(A)
println("The rank of your augmented matrix is $Ra")

if Ra == Rd
    println("The equation set which determined by matrix A has a solution.")
elseif Ra != Rd
    println("The equation set which determined by matrix A has no solution or has infinite solutions.")
end
