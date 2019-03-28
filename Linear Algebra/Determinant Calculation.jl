#### Determinant Calculation

using LinearAlgebra

# Input a n*n array as the determinant you want to calculate.
A = 
[
    4 2 3 5; 
    3 4 6 3;
    2 7 5 4;
    5 3 4 3
]

# Calculate the value of determinant
d = det(A)

println("The value of your determinant is ",d)