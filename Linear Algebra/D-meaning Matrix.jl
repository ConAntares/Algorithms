#### D-meaning Matrix

using LinearAlgebra

de_mean(n) = Matrix{Float64}(I, n, n) .- 1/n        # De-meaning Matrix
x = [0.2, 2.3, 1.0]

re = de_mean(length(x))*x                           # De-mean using Matrix Multiplication
println(re)                                         # [-0.966667, 1.13333, -0.166667]

rf = x .- sum(x)/length(x)                          # De-mean by Subtracting Mean
println(rf)                                         # [-0.966667, 1.13333, -0.166667]
