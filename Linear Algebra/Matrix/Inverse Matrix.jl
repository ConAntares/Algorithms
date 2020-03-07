#### Inverse Matrix.jl

using LinearAlgebra

# Input a array as the matrix you want to analysis
A = [1 6 4 3;
     6 2 1 9;
     5 4 6 6;
     4 5 2 5;]

# The value of determinant
re = det(A)
println("The determinant value of this matrix is $re.")

if re == 0
     println("This matrix is not invertible.")
else
     println("This matrix is invertible.")
     im = inv(A)
     println("This inverse matrix is \n$im.")
end