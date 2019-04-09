#### Algebraic Remainder of Sub-determinant

# Input a n*n array as the determinant you want to analysis.
D = 
[
    4 1 5 4 3;
    3 4 6 2 5;
    2 7 5 1 3;
    1 6 4 3 6;
    2 1 6 5 4
]
n = 5

# The number of sub-determinant's ordinal:
k = 3
# Input the ordinals of rows you want to extract:
I = [1,3,5]
# Input the ordinals of columns you want to extract:
J = [2,3,4]

## Fortran-like code:
# Initialize the sub-determinant:
S = zeros(k,k)
# Initialize the remainder:
M = zeros(n-k,n-k)
# Initialize the algebraic remainder:
A = zeros(n-k,n-k)
# Assign values to the sub-determinant:
a = 1
b = 1
for i in I
    for j in J
        global S[a,b] = D[i,j]
        global b = b + 1
    end
    global b = 1
    global a = a + 1
end
println("The sub-determinant is ", S)

## Julia-like code:
# Assign values to the sub-determinant:
S = view(D,I,J)
println("The sub-determinant is ", S)

# Assign values to the remainder and algebraic remainder:
N = range(1, stop=n)
Ip = setdiff(N,I)
Jp = setdiff(N,J)
M = view(D,Ip,Jp)
println("The of remainder is $M")
A = M*(-1)^(sum(I)+sum(J))
println("The of remainder is $A")
