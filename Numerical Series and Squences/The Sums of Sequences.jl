#### The Sums of Sequences

#  1. Calculate e using Taylor Series

to = time()

e = 1.0
f = 1.0
for n in 1:1000
    global f = n * f
    global e = e + 1/f
end

println("The Natural logarithm is $e.")
td = time() - to
println("The time interval is $td s.")

#  2. Calculate π using Taylor Series

to = time()

s = 0.0
for n in 0:10000000
    global s = s + (-1)^n/(2n+1)
end
π = 4s

println("The π is ",π)
td = time() - to
println("The time interval is $td s.")

#  3. Calcute the sum(n!/n^n)

to = time()

s = 0.0
u = Rational(1)
d = Rational(1)
for n in 1:4
    global u = n * u        # n!
    global d = n ^ n        # n^n
    global s = s + u/d
end

println("The result of sum(n!/n^n) is ",s)
td = time() - to
println("The time interval is $td s.")