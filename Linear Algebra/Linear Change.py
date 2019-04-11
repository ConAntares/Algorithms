#### Linear Change

## From x in [x_min,x_max] to y in [y_min,y_max]
# y=y_min+(x-x_min)(y_max-y_min)/(x_max-x_min)

import numpy as np

X = np.arange(0,11,1)           # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
print("X:")
for n in np.arange(0,11,1):
    print(X[n])

print("Y[n]=4*X[n]+20:")
Y = 4*X+10
for n in np.arange(0,11,1):
    print(Y[n])
