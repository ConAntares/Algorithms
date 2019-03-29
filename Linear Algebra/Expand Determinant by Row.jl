#### Expand Determinant by Row

using LinearAlgebra

# Input a n*n array as the determinant you want to analysis.
A = 
[
    4 2 3 5; 
    3 4 6 3;
    2 7 5 4;
    5 3 4 3
]
# The number of column
nCol = size(A,2)
# The number of row
nRow = size(A,1)

M = 5
# Expand the determinant by the first row
for c = 1:nCol
    for i = 1:nRow
        for j = 1:nCol
            if n<
                global M[i,j]=A[i-1,]
end

