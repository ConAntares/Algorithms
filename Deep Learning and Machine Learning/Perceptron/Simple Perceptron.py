#### Simple Perceptron

import numpy as np

# Received an AND function with parameters (x1, x2)
def AND(x1,x2):
    w1 = 0.5
    w2 = 0.5
    θ  = 0.75
    t  = x1*w1 + x2*w2
    if t <= θ:
        return 0
    elif t > θ:
        return 1

print(AND(0,0))     # 0
print(AND(0,1))     # 0
print(AND(1,0))     # 0
print(AND(1,1))     # 1


def OR(x1,x2):
    w1 = 0.5
    w2 = 0.5
    θ  = 0.25
    t  = x1*w1 + x2*w2
    if t <= θ:
        return 0
    elif t > θ:
        return 1

print(OR(0,0))     # 0
print(OR(0,1))     # 0
print(OR(1,0))     # 0
print(OR(1,1))     # 1

def NOT(x):
    w = 0.5
    θ = 0.25
    t = x * w
    if t <= θ:
        return 1
    elif t > θ:
        return 0

print(NOT(0))     # 1
print(NOT(1))     # 0

## Weight and Bias

x = np.array([0.0,1.0])     # Input
w = np.array([0.5,0.5])     # Weight
b = -0.75                   # Bias

re = w*x
print(re)
    # [0.  0.5]
re = np.sum(w*x) + b
print(re)
    # -0.25

def AND_plus(x1, x2):
    