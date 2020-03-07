#### Norm

import math
import numpy as np

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

def norm(x):
    return np.linalg.norm(x)

A = np.array([2,-1, 2])
r = norm(A)
print(r)        # 3.0

# RMS Value
"""
Definition
    rms(A) = ‖A‖/sqrt(n)
where n means the number of elements in Array A
"""

def rms(x):
    return np.linalg.norm(x) / math.sqrt(x.size)

r = rms(A)
print(r)        # 1.7320508075688774