#### Correlation Coefficient

import math
import numpy as np

# About Correlation Coefficient
"""
The correlation between two vectors A and B (with nonzero standard deviation) is defined as:
    ρ = Â'B̂ / (‖Â‖*‖B̂‖)
Where Â and B̂ are the de-meaned versions of A and B, respectively.
"""

def norm(x):
    return np.linalg.norm(x)

def correlation_coefficient(a,b):
    α = a - np.mean(a)
    β = b - np.mean(b)
    return np.dot(np.transpose(α), β) / (norm(α) * norm(β))

u = np.array([3.14, 1.59, 2.65, 3.58])
v = np.array([2.71, 8.28, 1.82, 8.45])

r = correlation_coefficient(u,v)
print(r)    # -0.16544050810663655

u = np.array([1.00, 2.00, 3.00, 4.00])
v = np.array([1.00, 2.00, 3.00, 4.00])

r = correlation_coefficient(u,v)
print(r)    # 0.9999999999999998

u = np.array([1.31, 2.41, 3.59, 4.26])
v = np.array([1.27, 2.18, 3.28, 4.18])

r = correlation_coefficient(u,v)
print(r)    # 0.9954845134896988