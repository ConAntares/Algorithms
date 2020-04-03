#### Taylor Approximation

## Description
"""
Consider the nonlinear function f:R^2 -> R^2 given by
    f(x) = [‖x-a‖; 
            ‖x-b‖]
         = [sqrt((x1-a1)^2-(x2-a2)^2);
            sqrt((x1-b1)^2-(x2-b2)^2)]
The two components of f give the distance of x to the points a and b. 
The function is differentiable, except when x = a or x = b, Its derivative or Jacobian matrix is given by
    Df(x) = [∂f1(z)/∂x1 ∂f1(z)/∂x2;
             ∂f2(z)/∂x1 ∂f2(z)/∂x2]
          = [(z1-a1)/‖z-a‖ (z2-a2)/‖z-a‖
             (z1-b1)/‖z-b‖ (z2-b2)/‖z-b‖]
Let's form the Taylor approximation of f for some specific values of a, b, and z, 
and then check it against the true value of f at a few points near z:
"""

using LinearAlgebra

f(x)  = [norm(x-a), norm(x-b)]
Df(z) = [(z-a)'/norm(z-a); (z-b)'/norm(z-b)]

f_hat(x) = f(z) + Df(z) * (x-z)

a = [1, 0]; b = [1, 1]; z = [0, 0] 

println(f([0.1, 0.1]))
    # [0.9055385138137417, 1.2727922061357855]

println(f_hat([0.1, 0.1]))
    # [0.9, 1.2727922061357857]

println(f([0.5, 0.5]))
    # [0.7071067811865476, 0.7071067811865476]

println(f_hat([0.5, 0.5]))
    # [0.5, 0.7071067811865477]