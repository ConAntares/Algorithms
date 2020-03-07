#### Distance

import math
import numpy as np

# About Distance
"""
The distance between two vectors is that:
    dist(A,B) = ‖A-B‖
"""

def norm(x):
    return np.linalg.norm(x)

u = np.array([1.8, 2.0,-3.6, 4.7])
v = np.array([0.6, 2.1, 1.9,-1.4])
w = np.array([2.0, 1.9,-4.0,-3.2])

print(norm(u-v))    # 8.30120473184465
print(norm(v-w))    # 6.328506932918696
print(norm(w-u))    # 7.913279977354524