# Calculate e using Taylor Series

o = time()
s = 1.0
f = 1.0

for n in 1:1000
    global f = n * f
    global s = s + 1/f
end

e = s
t = time()

println(e)
println("Time Interval: ",t-o," second")