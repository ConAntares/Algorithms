#### Trace

using LinearAlgebra

# Input a array as the matrix you want to analysis
A = [1 6 4 3;
     6 2 1 9;
     5 4 6 6;
     4 5 2 5;]

tr = sum(A[n,n] for n in 1:length(A[1,:]))
println("The trace of this matrix is $tr.")