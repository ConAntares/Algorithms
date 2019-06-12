#### Linear Functions

using LinearAlgebra

## Functions in Julia
f1(X) = X[1] + X[2] - X[4]^2

re = f1([-1,0,1,2])
println(re)         # -5

## Superposition
# Inner Product Function
A  = [-2, 0, 1, -3]
f2(X) = A' * X

re = f2([-1,0,1,2])
println(re)         # -3

X = [2, 2,-1,-1]
Y = [0, 1,-1, 0]
α = 1.2
β = -3.6

LHS = f2(α * X + β * Y)
println(LHS)    # 1.2000000000000002
RHS = α * f2(X) + β * f2(Y)
println(RHS)    # 1.2000000000000002

# Algebraic Average Function
avg(X) = (ones(length(X)) / length(X))' * X

re = avg([1, -3, 2, -1])
println(re)     # -0.25