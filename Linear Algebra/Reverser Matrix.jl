#### Reverser Matrix

using LinearAlgebra

reverser(n) = reverse(Matrix{Float64}(I, n, n), dims = 1)

reverser(4)