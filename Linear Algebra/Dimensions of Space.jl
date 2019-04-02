#### The Dimensions of Sub Space

using LinearAlgebra

# Input 2 matrices as your spaces (only homogeneous linear equations analyzed):
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

"""
proof: dim(V1+V2) = dim(V1) + dim(V1) - dim(V1∩V2)

Set a base of V1∩V2:    α(1),α(2),...,α(m);
Set a base of V1:       α(1),α(2),...,α(m),β(1),β(2),..,β(n1-m);
Set a base of V2:       α(1),α(2),...,α(m),γ(1),γ(2),..,γ(n2-m);
So, A base of V1+V2 is: α(1),α(2),...,α(m),β(1),β(2),..,β(n1-m),γ(2),..,γ(n2-m);
Set:                    k(1)α(1)+,...,+k(m)α(m)+p(1)β(1)+,...,+p(n1-m)β(n1-m)+q(1)γ(1)+,...,+q(n2-m)γ(n2-m) = 0;
Then, we have:          q(1)γ(1)+,...,+q(n2-m)γ(n2-m) = -(k(1)α(1)+,...,+k(m)α(m)+p(1)β(1)+,...,+p(n1-m)β(n1-m));
Since:                  q(1)γ(1)+,...,+q(n2-m)γ(n2-m) ∈ V2,
                        k(1)α(1)+,...,+k(m)α(m)+p(1)β(1)+,...,+p(n1-m)β(n1-m) ∈ V1;
Then they ∈ V1∩V2;
∃(l(1),..,l(m)):        q(1)γ(1)+,...,+q(n2-m)γ(n2-m) = l(1)α(1)+,...,+l(m)α(m);
Since:                  α(1),α(2),...,α(m),γ(1),γ(2),..,γ(n2-m) is linear independent;
Then:                   q(1),q(2),...,q(n2-m) = 0;
And:                    k(1)α(1)+,...,+k(m)α(m)+p(1)β(1)+,...,+p(n1-m)β(n1-m) = 0;
Since:                  α(1),α(2),...,α(m),β(1),β(2),..,β(n1-m) is linear independent;
Then:                   k(1),k(2),...,k(m),p(1),p(2),...,p(n1-m) = 0;
We get:                 α(1),α(2),...,α(m),β(1),β(2),..,β(n1-m),γ(2),..,γ(n2-m) is linear independent;
So;                     dim(V1+V2) = m + (n1-m) + (n2-m) = m + n1 + n2,
                        dim(V1+V2) = dim(V1) + dim(V1) - dim(V1∩V2).
□
"""