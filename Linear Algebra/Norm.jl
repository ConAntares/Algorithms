#### Norm

using LinearAlgebra

# Definition:
"""
‖A‖ = sqrt(ΣiΣj(|A[i,j]|^2))
"""
# Properties
"""
‖A‖ ≥ 0
‖A‖ = 0 iff A = O
‖aA‖ = |a| * ‖A‖
‖A + B‖ ≤ ‖A‖ + ‖B‖
"""

x = [2,-1, 2]
r = norm(x)
println(r)      # 3.0