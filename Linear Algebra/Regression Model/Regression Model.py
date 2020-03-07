#### Regression Model

import math
import numpy as np

# About Regression Model
"""
Regression Model is the affine function of x given by
    f(x) = x'β + v
where the n-vector β and the scalar v are the parameters in the model.
Regression Model is used to guess or approximate a real or observed value
of the number y that is associated with x.
"""

# Parameters
β = np.array([148.73, -18.85])
v = 54.40

def ŷ(x):
    return np.dot(np.transpose(x),β) + v

# Evaluate Regression Model Prediction
x = np.array([0.846, 1])
y = 115

re = ŷ(x)
print(re)       # 161.37557999999999