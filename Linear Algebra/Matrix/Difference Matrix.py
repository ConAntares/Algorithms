#### Difference Matrix

# About Difference Matrix
"""
An (n-1)×n difference matrix can be constructed in several ways. A simple one is the following.
"""

import numpy as np

def difference_matrix(n):
    return np.hstack((-np.eye(n-1,n-1),np.array([np.zeros(n-1)]).T)) + np.hstack((np.array([np.zeros(n-1)]).T,np.eye(n-1,n-1)))

print(difference_matrix(4))
