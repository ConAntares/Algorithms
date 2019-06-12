#### Linear Combination

import numpy as np

def lincomb(coeff, vectors):
    n = vectors[1].size
    r = np.zeros(n)
    for i in range(0,len(vectors)):
        r = r + coeff[i] * vectors[i]
    return r

re = lincomb((np.array([-0.5, 1.5])), (np.array([1, 2]), np.array([3, 4])))

print(re)       # [4. 5.]