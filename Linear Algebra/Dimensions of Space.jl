#### The Dimensions of Sub Space

using LinearAlgebra

# Input 2 matrixs as your spaces (only homogeneous linear equations analyzed):
S1 = [1 2 -1;]  # x + 2y -z = 0, z = x + 2y
S2 = [2 1 -2;]  # 2x + y -2z = 0, z  = x + 1/2y

# Intersection:
Si = [S1;S2]

# The ranks of spaces:
R1 = rank(S1)
R2 = rank(S2)
Ri = rank(Si)

# The numbers of unknowns:
n1 = size(S1,2)
n2 = size(S2,2)
ni = size(Si,2)

# The dimensions of solution spaces
D1 = n1 - R1
D2 = n2 - R2
Di = ni - Ri        # Intersection
Da = D1 + D2 - Di   # Sum

println("The dimension of solution space of your first equation set is $D1,")
println("The dimension of solution space of your second equation set is $D2,")
println("The dimension of solution space of the intersection is $Di,")
println("The dimension of solution space of the sum is $Da,")
