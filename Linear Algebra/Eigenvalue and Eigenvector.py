#### Eigenvalue and Eigenvector

import numpy as np

"""
A|V⟩ = λ|V⟩
λ: Eigenvalue
V: Eigenvector
"""

A = np.array([[3.14, 1.59, 2.65],
              [2.71, 8.28, 1.82],
              [6.62, 6.06, 8.96]])

print("The Source Matrix：\n{}".format(A))

λ, V = np.linalg.eig(A)

print("The eigenvalues：\n{}" .format(λ))
print("The eigenvectors：\n{}".format(V))

print("\nPrint every eigenvalues and the corresponding eigenvectors.\n")
for n in range(0,len(V)):
    val = λ[n]
    vec = V[:,n]
    lhs = np.dot(A,  vec)
    rhs = np.dot(val,vec)
    print("The eigenvalue: %f corresponds eigenvector:" %val, vec, ";")
    print("Then, A|V⟩ equals:", lhs, "and λ|V⟩ equals:", rhs, ".\n")