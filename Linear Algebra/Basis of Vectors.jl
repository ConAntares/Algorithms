#### Basis of Vectors

using LinearAlgebra

"""
We suppose:
    C  = αE + βA + γB
    c1 = α + β
    c2 = βa + γ
    c3 = γa
We get:
    γ  = c3/a
    c2 = βa + γ = βa + c3/a
    β  = c2/a - c3/a^2
    c1 = α + β = α + c2/a - c3/a^2
    α  = c1 - c2/a + c3/a^2
"""

# Determine the Basis
r = 0.05; a = -(1+r)
E = [1, 0, 0]
A = [1, a, 0]
B = [0, 1, a]
C = [1, 2,-3]

# Coefficients of expansion
α = C[1] - C[2]/a + C[3]/a^2
β = C[2]/a - C[3]/a^2
γ = C[3]/a

R = α*E + β*A + γ*B
println(R)      # [1.0, 2.0, -3.0]