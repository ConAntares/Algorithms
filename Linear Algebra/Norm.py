#### Norm

import math
import numpy as np

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

x = np.array([2,-1, 2])
r = np.linalg.norm(x)
print(r)        # 3.0