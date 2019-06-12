#### Angle

using LinearAlgebra

# Define the angle function, which returns radians:
angle(A,B) = acos(A' * B / (norm(A) * norm(B)))

u = [1, 2,-1]
v = [2, 0,-3]

re = angle(u,v)
println(re)         # 0.9689825515916383

angle_to_degree(x) = x * 360 / (2 * pi)
degree_to_angle(x) = x * (2 * pi) / 360

ri = angle_to_degree(re)
rj = degree_to_angle(ri)
println(ri)         # 55.51861062801842
println(rj)         # 0.9689825515916383