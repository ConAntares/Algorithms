#### Set

import numpy as np

listA = [1, 2, 3, 4, 5, 1, 3, 5]
re = set(listA)
print(re)
    # {1, 2, 3, 4, 5}
print(type(re))
    # <class 'set'>
print(len(re))
    # 5
re.add(6)
print(re)
    # {1, 2, 3, 4, 5, 6}
re.remove(6)
print(re)
    # {1, 2, 3, 4, 5}

A = set([1,2,3,4])
B = set([1,3,5,7])
re = A & B
print(re)
    # {1, 3}
re = A | B
print(re)
    # {1, 2, 3, 4, 5, 7}
re = A^B
print(re)
    # {2, 4, 5, 7}