#### Angle

import math
import numpy as np

# Define the norm:
def norm(x):
    return np.linalg.norm(x)

# Define the angle function, which returns radians:
def angle(A,B):
    return math.acos(np.dot(np.transpose(A), B) / (norm(A) * norm(B)))

u = np.array([1, 2,-1])
v = np.array([2, 0,-3])

re = angle(u,v)
print(re)           # 0.9689825515916383

def angle_to_degree(x):
    return x * 360 / (2 * math.pi)

def degree_to_angle(x):
    return x * (2 * math.pi) / 360

ri = angle_to_degree(re)
rj = degree_to_angle(ri)
print(ri)           # 55.51861062801842
print(rj)           # 0.9689825515916383
