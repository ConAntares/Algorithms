#### Matrix Elimination and LU Decomposition

using LinearAlgebra

# Input a n*n array as the determinant you want to analysis.
D = [ 4 1 5 4 3;
      3 4 6 2 5;
      2 7 5 1 3;
      1 6 4 3 6;
      2 1 6 5 4 ]

L, U = lu(D)
println(U)
    # [4.0 1.0  5.0   4.0      3.0; 
    #  0.0 3.25 2.25 -1.0      2.75; 
    #  0.0 0.0 -2.0   1.0     -4.0; 
    #  0.0 0.0  0.0   3.15385  2.84615; 
    #  0.0 0.0  0.0   0.0     -8.5]

B, T = factorize(D)
println(T)
    # [4.0 1.0  5.0   4.0      3.0; 
    #  0.0 3.25 2.25 -1.0      2.75; 
    #  0.0 0.0 -2.0   1.0     -4.0; 
    #  0.0 0.0  0.0   3.15385  2.84615; 
    #  0.0 0.0  0.0   0.0     -8.5]