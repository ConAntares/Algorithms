#### Fibonacci Sequence

"""
f(n) =  1                   (n = 1)
        1                   (n = 2)
        f(n-1) + f(n-2)     (n > 2)
"""

## Fibonacci Sequence with Number

using Plots; pyplot()

function fib1(n::BigInt)
    a = b = c = BigInt(1)
    if n <= 0
        throw(DomainError(n, "Please input a positive integer."))
        return -1
    end
    while (n-2) > 0
        c = a + b
        a = b
        b = c
        n = n - 1
    end
    return c
end

function fib2(n::BigInt)
    a = b = c = BigInt(1)
    if n <= 0
        throw(DomainError(n, "Please input a positive integer."))
        return -1
    end
    for i in 3:n
        c = a + b
        a = b
        b = c
    end
    return c
end

function fib3(n::BigInt)
    if n <= 0
        throw(DomainError(n, "Please input a positive integer."))
        return -1
    elseif 1 <= n <= 2
        return 1
    else
        return fib1(n-1) + fib1(n-2)
    end
end

function fib4(n::BigInt)
    if n <= 0
        throw(DomainError(n, "Please input a positive integer."))
        return -1
    elseif 1 <= n <= 2
        return 1
    end
    return fib2(n-1) + fib2(n-2)
end

println("Please input a positive integer.")
number = parse(BigInt, chomp(readline()))

re = fib1(number)

if re != -1
    println("The fibonacci sequence of $number is $re.")
end

## Fibonacci Sequence in Array

N = 1:1:20
M = [fib1(n) for n in N]

@timev(M1 = [fib1(n) for n in N])
# @timev(M2 = [fib2(n) for n in N])
# @timev(M3 = [fib3(n) for n in N])
# @timev(M4 = [fib4(n) for n in N])

plot(fontfamily=("Serif"),dpi=1024)
plot!(N,M,color="#00B4DC",label="Fibonacci Sequence")