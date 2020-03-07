#### Clustering

import math
import numpy as np

def norm(x):
    return np.linalg.norm(x)

def JCluster(X, reps, assignment):
    t = 0
    c = 0
    for i in range(0, len(X)):
        c = c + norm(X[i] - reps[assignment[i]])**2
        t = t + 1
    r = c / t
    return r

def JCluster_plus(X, reps, assignment):
    return np.mean([norm(X[i] - reps[assignment[i]])**2 for i in range(0, len(X))])

U = np.array([[ 0, 1],
              [ 1, 0],
              [-1, 1]])

R = np.array([[ 1, 1],
              [ 0, 0]])

S = np.array([1, 2 ,1])
A = S - 1

re = JCluster(U, R, A)
print(re)             # 2.0

re = JCluster_plus(U, R, A)
print(re)             # 2.0
