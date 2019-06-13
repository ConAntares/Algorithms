#### Clustering

using LinearAlgebra
using Statistics

function JClust(X, reps, assignment)
    return mean([norm(X[i] - reps[assignment[i]])^2 for i = 1:length(X)])
end

U = [[ 0, 1],
     [ 1, 0],
     [-1, 1]]

R = [[ 1, 1],
     [ 0, 0]]

A = [1, 2, 1]

re = JClust(U, R, A)
println(re)             # 2.0