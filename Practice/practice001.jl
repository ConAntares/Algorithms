# Calcute the sum(n!/n^n)

s = Rational(0)
u = Rational(1)
d = Rational(1)

for n in 1:8
    global u = n * u        # n!
    global d = n ^ n        # n^n
    t = u//d
    global s = s + t
    println(t)
end

e = s

println("The result is ",e)