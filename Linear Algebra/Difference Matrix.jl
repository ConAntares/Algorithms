#### Difference Matrix

# About Difference Matrix
"""
An (n-1)×n difference matrix can be constructed in several ways. A simple one is the following.
"""

using LinearAlgebra

difference_matrix(n) = [-Matrix{Float64}(I, n-1, n-1) zeros(n-1)] + [zeros(n-1) Matrix{Float64}(I, n-1, n-1)]

println(difference_matrix(4))