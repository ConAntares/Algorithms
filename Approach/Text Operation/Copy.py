#### Copy

import numpy as np
import copy

A = [0,2,4,8,[1,3]]
print(A)    # [0, 2, 4, 8, [1, 3]]

E = A
C = copy.copy(A)
D = copy.deepcopy(A)

A.append(16)
print(A)        # [0, 2, 4, 8, [1, 3], 16]
print(E)        # [0, 2, 4, 8, [1, 3], 16]
print(C)        # [0, 2, 4, 8, [1, 3]]
print(D)        # [0, 2, 4, 8, [1, 3]]

A[4].append(6)
print(A)        # [0, 2, 4, 8, [1, 3, 6], 16]
print(E)        # [0, 2, 4, 8, [1, 3, 6], 16]
print(C)        # [0, 2, 4, 8, [1, 3, 6]]
print(D)        # [0, 2, 4, 8, [1, 3]]

print(id(A))    # 1217355093000
print(id(E))    # 1217355093000
print(id(C))    # 1217355101576
print(id(D))    # 1217345121864