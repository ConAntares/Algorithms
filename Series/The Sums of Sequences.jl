#  0. Time Interval Setting
time_o = time()

#  1. Calculate e using Taylor Series
e = 1.0
f = 1.0
for n in 1:1000
    global f = n * f
    global e = e + 1/f
end
t = time()
println("The Natural logarithm is ",e)

#  2. Calculate π using Taylor Series
s = 0.0
for n in 0:10000000
    global s = s + (-1)^n/(2n+1)
end
π = 4s
println("The π is ",π)

#  3. Calcute the sum(n!/n^n)
s = 0.0
u = Rational(1)
d = Rational(1)
for n in 1:4
    global u = n * u        # n!
    global d = n ^ n        # n^n
    global s = s + u/d
end
println("The result of sum(n!/n^n) is ",s)

#  0. Time Interval Setting
time_t = time()
println("Time Interval: ",time_t-time_o," second")