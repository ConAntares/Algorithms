#### Linear Dynamic System

"""
Let's simulate a time-invariant linear dynamic system
    x(t+1) = Ax(t), t = 1,...,T,...
"""

using Plots; pyplot()

x_1 = [ 1, 0, -1]   # Initinal state
n = length(x_1)
T = 50
A = [ 0.97  0.10 -0.05;
     -0.30  0.99  0.05;
      0.01 -0.04  0.96]

state_traj = [x_1 zeros(n,T-1)]

for t=1:T-1         # Dynamics recursion
    state_traj[:,t+1] = A*state_traj[:,t]
    # println(t, state_traj, "\n")
end

plot(1:T, state_traj', xlabel="t", label=["(x_t)_1", "(x_t)_2", "(x_t)_3"])