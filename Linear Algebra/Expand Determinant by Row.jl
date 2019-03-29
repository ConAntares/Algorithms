#### Expand Determinant by Row

# Input a n*n array as the determinant you want to analysis.
D = 
[
    4 2 3;
    3 4 6;
    2 7 5;
]
# The number of row
nRow = size(D,1)
# The number of column
nCol = size(D,2)

# Initialize the remainder
M = zeros(nRow-1,nCol-1)
# Initialize algebraic remainder
A = zeros(nRow-1,nCol-1)

for n = 1:nCol              # D[1,1], D[1,2], ... , D[1,n]
    for i = 1:nRow-1
        for j = 1:nCol-1
            if n <= j
                global M[i,j] = D[i+1,j+1]
            elseif n > j
                global M[i,j] = D[i+1,j]
            end
        end
    end
    A = (-1)^(1+n)*M
    println("The of remainder D[$n] is $M")
    println("The of algebraic remainder D[$n] is $A")
end