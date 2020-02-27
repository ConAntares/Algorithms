#### Cppy

# The source vector
S = [1, 2, 3, 4]

# Copying
X = copy(S)

# Equality
Y = S

# Change the source
S[4] = 5

println(X)      # [1, 2, 3, 4]
println(Y)      # [1, 2, 3, 5]

println(X==S)   # false
println(Y==S)   # true