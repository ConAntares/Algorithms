#### Expansion in an Orthonormal Basis

using LinearAlgebra

α = [0, 0,-1]
β = [1, 1, 0]/sqrt(2)
γ = [1,-1, 0]/sqrt(2)

X = [5, 6, 8]
a = α'*X; b = β'*X; c = γ'*X

# Expansion of X in Basis(α,β,γ)
R = a*α + b*β + c*γ

println(R)  # [5.0, 6.0, 8.0]