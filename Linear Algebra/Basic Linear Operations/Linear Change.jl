#### Linear Change

## From x in [x_min,x_max] to y in [y_min,y_max]
# y=y_min+(x-x_min)(y_max-y_min)/(x_max-x_min)

X = range(0,stop=10,step=1)
println("X:")
for n in 1:11
    print(X[n],"\t")
end
println()

println("Y[n]=4*X[n]+20:")
Y = [4*X[n]+10 for n in 1:11]
for n in 1:11
    print(Y[n],"\t")
end
println()
