#### Price elasticity of demand

p = [  10,   20,   15]              # Current prices
d = [ 5.6,  1.5,  8.6]              # Current demand (in thousands)
c = [ 6.5, 11.2,  9.8]              # Cost to manufacture

profit = (p-c)'*d                   # Current total profit
println(profit)                     # 77.52

# Demand elasticity matrix
E = [-0.3   0.1  -0.10;
      0.1  -0.5   0.05;
     -0.1  -0.05 -0.4  ]
    
p_new = [ 9, 21, 14]                # Proposed new prices
Δ_p = (p_new - p)./ p               # Fractional change in prices
Δ_d = E * Δ_p                       # Predicted fractional change in demand

d_new = d.* (1 .+ Δ_d)              # Predicted new demand
profit_new = (p_new - c)' * d_new   # Predicted new profit

println(profit_new)                 # 66.07393333333333