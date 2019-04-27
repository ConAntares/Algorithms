#### Factorial

using Plots; pyplot()

function fac1(n::BigInt)
    o = r = BigInt(1)
    if n < 0
        throw(DomainError(n, "Please input a positive integer."))
        return -1
    elseif n in [0,1]
        return 1
    end
    while n >= 2
        r = n * r
        n = n - 1
    end
    return r
end

function fac2(n::BigInt)
    o = r = BigInt(1)
    if n < 0
        throw(DomainError(n, "Please input a positive integer."))
        return -1
    elseif n in [0,1]
        return 1
    end
    for i in 2:n
        r = r * i
    end
    return r
end

println("Please input a positive integer.")
number = parse(BigInt, chomp(readline()))

re = fac2(number)

if re != -1
    println("The factorial of $number is $re.")
end

N = 1:1:20
M = [fac1(n) for n in N]

@timev(M1 = [fac1(n) for n in N])
@timev(M2 = [fac2(n) for n in N])

plot(fontfamily=("Serif"),dpi=1024)
plot!(N,M,color="#00B4DC",label="Factorial")