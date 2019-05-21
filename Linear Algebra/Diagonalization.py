#### Diagonalization

import numpy as np

A = np.array([[3.14, 1.59, 2.65],
              [2.71, 8.28, 1.82],
              [6.62, 6.06, 8.96]])

print("The Source Matrix：\n{}".format(A))

λ, V = np.linalg.eig(A)

print("The eigenvalues：\n{}" .format(λ))
print("The eigenvectors：\n{}".format(V))

E = set(λ)
if len(E) == len(A):
    print("This matrix can be diagonalized.")
elif len(E) != len(A):
    print("This matrix cannot be diagonalized.")

print()

Λ = np.dot(np.dot(np.linalg.inv(V), A),V)
print("The diagonalized matrix is: \n",Λ)

D = np.diag(λ)
print("The diagonalized matrix is: \n",D)