#### k-means Algorithm

using LinearAlgebra
using Statistics

function kmeans(X, k; maxiters = 100, tol= 1e-5) 
    N = length(X)
    n = length(X[1])
    distances = zeros(N)            # Used to store the distance of each point to the nearest representative. 
    reps = [zeros(n) for j = 1:k]   # Used to store representatives.
    assignment = [rand(1:k) for i = 1: N]
        # assignment is an array of N integers between 1 and k;
        # The initial assignment is chosen randomly.
end