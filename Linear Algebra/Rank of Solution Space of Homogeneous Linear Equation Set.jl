#### The Rank of Solution Space of Homogeneous Linear Equation Set

using LinearAlgebra

# Input a array as the matrix you want to analysis.
D = [ 4 2 3 4;
      3 4 5 5;
      5 3 6 6;
      3 3 9 6;
      8 2 4 8;
      2 4 9 5 ]
# The rank of your matrix:
Rd = rank(D)
# The number of unknown numbers:
n = size(D,2)
# The rank of solution space of homogeneous linear equation set
Rw = n - Rd

if Rd == n
    println("The homogeneous linear equation set has zeros solutions." )
elseif Rd < n
    println("The homogeneous linear equation set has infinite solutions." )
end

println("The rank of solution space of homogeneous linear equation set is $Rw." )
