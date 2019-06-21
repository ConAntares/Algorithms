#### Expansion in an Orthonormal Basis

import math
import numpy as np

α = np.array([0, 0,-1])
β = np.array([1, 1, 0])/2**(1/2)
γ = np.array([1,-1, 0])/2**(1/2)

X = np.array([5, 6, 8])
a = α.T*X; b = β.T*X; c = γ.T*X

# Expansion of X in Basis(α,β,γ)
R = a*α + b*β + c*γ

print(R)    # [5.0, 6.0, 8.0]