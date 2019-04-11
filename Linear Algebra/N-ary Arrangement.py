#### N-ary Arrangement

import numpy as np

# Input a Vector as Sequence:
A = np.array([2,4,3,1])
print("The sequence is ",A)
# Print the elements number of the Vector:
print("The number of elements is ",A.shape[0])

# Initialize the Order Number:
o = int(0)
# Initialize the Reverse Order Number:
t = int(0)

# Calculus the Order Number and the Reverse Order Number:
for i in np.arange(0,A.shape[0]):
    for j in np.arange(0,i):
        # print(i,j)
        if A[j] < A[i]:
            o = o + 1
        elif A[j] > A[i]:
            t = t + 1
print("The Order Number of this Sequence is: ",o)
print("The Reverse Order Number of this Sequence is: ",t)

# Determine whether the sequence is odd or even:
if np.remainder(0,2) == 0:
    print("This Sequence is even.")
elif  np.remainder(0,1) == 0:
    print("This Sequence is odd.")