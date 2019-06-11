#### Orthogonal matrix

using LinearAlgebra

# Input a n*n array as the matrix you want to analysis.
D = [1 0 0;
     0 0 1;
     0 1 0;]

re = det(D)
println("The determinant value of this matrix is $re.")

if re == 0
    println("This matrix is not invertible.")
else
    println("This matrix is invertible.")
    if inv(D) == D'
        println("This matrix is orthogonal.")
    else
        println("This matrix is not orthogonal.")
    end
end
