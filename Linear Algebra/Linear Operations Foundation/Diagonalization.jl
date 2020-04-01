#### Diagonalization

using LinearAlgebra

A = [3.14 1.59 2.65;
     2.71 8.28 1.82;
     6.62 6.06 8.96]

println("The Source Matrix is \n$A.")

λ = eigvals(A)
println("The eigenvalues：\n$λ")
     
V = eigvecs(A)
println("The eigenvectors: \n$V")

E = Set(λ)
if length(E) == length(A[1,:])
    println("This matrix can be diagonalized.")
elseif length(E) == length(A[1,:])
    println("This matrix cannot be diagonalized.")
end

Λ = inv(V) * A * V
println("The diagonalized matrix is: \n",Λ)

D = Diagonal(λ)
println("The diagonalized matrix is: \n",D)