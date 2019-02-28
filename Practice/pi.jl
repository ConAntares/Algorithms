# Calculate π using Taylor Series

o = time()
s = 0.0

for n in 0:10000000
#    println(((-1)^n//(2n+1)))
    global s = s + (-1)^n/(2n+1)
end

pi = 4s
t = time()

println(pi)
println("Time Interval: ",t-o," second")