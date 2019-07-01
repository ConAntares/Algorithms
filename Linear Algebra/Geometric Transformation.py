#### Geometric Transformation

import math
import numpy as np

def rot(θ):
    return np.array([[math.cos(θ),-math.sin(θ)],[math.sin(θ), math.cos(θ)]])

θ = math.pi/3

A = [[1,0],[1.5,0],[2,0],[1,0.25],[1.5,0.25],[1,0.5]]
R = [np.dot(rot(θ),p) for p in A]

print(R)
    # [array([0.5       , 0.8660254]), 
    #  array([0.75      , 1.29903811]), 
    #  array([1.        , 1.73205081]), 
    #  array([0.28349365, 0.9910254 ]), 
    #  array([0.53349365, 1.42403811]), 
    #  array([0.0669873 , 1.1160254])]