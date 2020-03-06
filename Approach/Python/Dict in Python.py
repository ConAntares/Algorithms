#### Dict

import numpy as np

re = {1:1.1, 2:2.2, 3:3.3, 4:4.4}
print(re)
    # {1: 1.1, 2: 2.2, 3: 3.3}
print(type(re))
    # <class 'dict'>
print(len(re))
    # 4
re[5] = 5.5
print(re)
    # {1: 1.1, 2: 2.2, 3: 3.3, 4: 4.4, 5: 5.5}

re = {i:i**2 for i in np.arange(1,5,1)}
print(re)
    # {1: 1, 2: 4, 3: 9, 4: 16}
print(re[1],re[2],re[3],re[4])
    # 1 4 9 16