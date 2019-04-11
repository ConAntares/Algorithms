#### Solve Linear Equations

"""
In general, a linear equation system can be written on the form:
    A(m,n)*X(n*1)=B(m*1)
"""

using LinearAlgebra

# Input a m*n array as the coefficient term matrix
A = [1 6 4 3;
     6 2 1 9;
     5 4 6 6;
     4 5 2 5;]

# Input a m*1 array as the constant term matrix
B = [4;3;6;1]
# The augmented matrix
J = hcat(A,B)
# A zeros vector:
Z = zeros(size(B,1),1)
if iszero(B) == true
    println("The original equation set is homogeneous.")
elseif iszero(B) == false
    println("The original equation set is not homogeneous.")
end

# The rank of coefficient term matrix
Ra = rank(A)
# Calculate the value of determinant
Da = det(A)