#### Geometric Transformation

using Plots; plotlyjs()

rot(θ) = [cos(θ) -sin(θ);
          sin(θ)  cos(θ)]

θ = pi/3

A = [[1,0],[1.5,0],[2,0],[1,0.25],[1.5,0.25],[1,0.5]]
R = [rot(θ)*p for p in A]

Xa = [c[1] for c in A]; Ya = [c[2] for c in A]
Xr = [c[1] for c in R]; Yr = [c[2] for c in R]

scatter(Xa, Ya)
scatter!(Xr, Yr)