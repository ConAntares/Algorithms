#### Norm

using LinearAlgebra

# Norm
"""
Definition
    ‖A‖ = sqrt(ΣiΣj(|A[i,j]|^2))
Properties
    ‖A‖ ≥ 0
    ‖A‖ = 0 iff A = O
    ‖aA‖ = |a| * ‖A‖
    ‖A + B‖ ≤ ‖A‖ + ‖B‖
"""

A = [2,-1, 2]
r = norm(A)
println(r)      # 3.0

# RMS Value
"""
Definition
    rms(A) = ‖A‖/sqrt(n)
where n means the number of elements in Array A
"""

rms(x) = norm(x) / sqrt(length(x))
r = rms(A)
println(r)      # 1.7320508075688774