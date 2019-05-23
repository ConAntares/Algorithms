#### Simple Perceptron with Weight and Bias

import numpy as np

x = np.array([0.0,1.0])     # Input
w = np.array([0.5,0.5])     # Weight
b = -0.75                   # Bias

re = w*x
print(re)
    # [0.  0.5]
re = np.sum(w*x) + b
print(re)
    # -0.25

# def AND_plus(x1, x2):