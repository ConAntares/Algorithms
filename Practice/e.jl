# Calculate e using Taylor Series

s = 1.0
f = 1.0

for n in 1:100
    global f = n * f
    global s = s + 1/f
end

e = s

println(e)