#### Incidence Matrix

A = [-1 -1  0  1  0;
      1  0 -1  0  0;
      0  0  1 -1 -1;
      0  1  0  0  1]

xCric = [1,-1, 1, 0, 1]

Re = A * xCric
println(Re)     # [0, 0, 0, 0]
