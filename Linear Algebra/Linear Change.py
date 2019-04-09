#### Linear Change

## From x in [x_min,x_max] to y in [y_min,y_max]
# y=y_min+(x-x_min)(y_max-y_min)/(x_max-x_min)

#%%
import numpy as np

X = np.arange(0,11,1)           # range(0,stop=10,step=1)
print("X:")
for n in np.arange(0,11,1):
    print(X[n])

print("Y[n]=4*X[n]+20:")
Y = 4*X+10
for n in np.arange(0,11,1):
    print(Y[n])