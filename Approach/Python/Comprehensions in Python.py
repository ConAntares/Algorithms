#### Comprehensions

import numpy as np

re = [i for i in range(10)]
print(re)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

re = [i for i in np.arange(0,10,1)]
print(re)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict
re = {i: i % 2 == 0 for i in np.arange(0,4)}
print(re)
    # {0: True, 1: False, 2: True, 3: False}

## Set
re = {i for i in [1,1,2,3,4,4,4,3,4,1,2,3]}
print(re)
    # {1, 2, 3, 4, 5, 6, 7, 8}
