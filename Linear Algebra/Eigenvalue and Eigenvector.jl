#### Eigenvalue and Eigenvector

using LinearAlgebra

"""
A|V⟩ = λ|V⟩
λ: Eigenvalue
V: Eigenvector
"""

A = [3.14 1.59 2.65;
     2.71 8.28 1.82;
     6.62 6.06 8.96]

println("The Source Matrix is \n$A.")

λ = eigvals(A)
println("The eigenvalues：\n$λ")

V = eigvecs(A)
println("The eigenvectors: \n$V")

println("\nPrint every eigenvalues and the corresponding eigenvectors.\n")
for n in 1:length(A[1,:])
    val = λ[n]
    vec = V[:,n]
    lhs = A * vec
    rhs = val * vec
    println("The eigenvalue: $val corresponds eigenvector: $vec;")
    println("Then, A|V⟩ equals: $lhs and λ|V⟩ equals: $rhs.\n")
end
