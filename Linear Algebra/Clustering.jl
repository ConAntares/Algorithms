#### Clustering

using LinearAlgebra
using Statistics

function JCluster(X, reps, assignment)
     t = 0
     c = 0
     for i in 1:length(X)
          c = c + norm(X[i] - reps[assignment[i]])^2
          t = t + 1
     end
     r = c / t
     return r
end

function JCluster_plus(X, reps, assignment)
    return mean([norm(X[i] - reps[assignment[i]])^2 for i = 1:length(X)])
end

JCluster_pro(X, reps, assignment) = mean([norm(X[i] - reps[assignment[i]])^2 for i = 1:length(X)])

U = [[ 0, 1],
     [ 1, 0],
     [-1, 1]]

R = [[ 1, 1],
     [ 0, 0]]

A = [1, 2, 1]

re = JCluster(U, R, A)
println(re)             # 2.0

re = JCluster_plus(U, R, A)
println(re)             # 2.0

re = JCluster_pro(U, R, A)
println(re)             # 2.0

@time JCluster(U, R, A)
@time JCluster_plus(U, R, A)
@time JCluster_pro(U, R, A)