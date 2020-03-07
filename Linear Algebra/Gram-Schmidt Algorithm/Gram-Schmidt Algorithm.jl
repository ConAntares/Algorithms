#### Gram-Schmidt Algorithm

# About Gram-Schmidt Algorithm
"""
In this section we describe an algorithm that can be used to determine if a list of n-vectors A(1),...,A(k) is linearly independent.
In later chapters we will see that it has many other uses as well.
The algorithm is named after the mathematicians Jorgen Pedersen Gram and Erhard Schmidt, although it was already known before their work.

If the vectors are linearly independent, the Gram-Schmidt algorithm produces an orthonormal collection of vectors Q(1),...,Q(k) with the following properties:
For each i = 1,...,k; A(i) is a linear combination of Q(1),...,Q(i), and Q(i) is a linear combination of A(1),...,A(i).
If the vectors A(1),...,A(j-1) are linearly independent but A(1),...,A(j) are linearly dependent, the algorithm detects this and terminates.
Inother words, the Gram-Schmidt algorithm finds the first vector A(j) that is a linear combination of previous vectors A(1),...,A(j-1).
"""

# Description for Gram-Schmidt Algorithm
"""
given n-vectors A(1),...,A(k).
for i = 1,...,k:
    1. Orthogonalization: Qt(i) = A(i) - Q'(1)A(i)Q(1) - Q'(2)A(i)Q(2) - ... - Q'(i-1)A(i)Q(i-1);
    2. Test for linear dependence: if Qt(i) = 0, quit;
    3. Normalization: Q(i) = Qt(i)/norm(Qt(i)).
"""

using LinearAlgebra

function gram_schmidt(A)
    Q = []
    τ = 1e-10
    for i = 1:length(A)
        Qt = A[i]
        for j = 1:i-1
            Qt = Qt - Q[j]'*A[i]*Q[j]
        end
        if norm(Qt) < τ
            println("Vectors are linearly dependent.")
            return Q
        end
        push!(Q, Qt/norm(Qt))
    end
    return Q
end

a = [[-1, 1,-1, 1],
     [-1, 3,-1, 3],
     [ 1, 3, 5, 7]]

q = gram_schmidt(a)
println(q)