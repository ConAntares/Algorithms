#### Dirichlet Energy

using LinearAlgebra

A = [-1 -1  0  1  0;
      1  0 -1  0  0;
      0  0  1 -1 -1;
      0  1  0  0  1]

VSmooth = [1, 2, 2, 1]
VRough  = [1,-1, 2,-1]

nSmooth = norm(A'*VSmooth)^2
nRough  = norm(A'*VRough)^2

println(nSmooth,"\n",nRough)
      # 2.9999999999999996
      # 27.0