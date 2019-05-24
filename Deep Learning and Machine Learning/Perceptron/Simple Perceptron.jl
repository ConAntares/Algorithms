#### Simple Perceptron

# Received an AND function with parameters (x1, x2)

function AND(x1,x2)
    w1 = 0.5
    w2 = 0.5
    θ  = 0.75
    t  = x1*w1 + x2*w2
    if t <= θ
        return 0
    elseif t > θ
        return 1
    end
end

println(AND(0,0))   # 0
println(AND(0,1))   # 0
println(AND(1,0))   # 0
println(AND(1,1))   # 1

function OR(x1,x2)
    w1 = 0.5
    w2 = 0.5
    θ  = 0.25
    t  = x1*w1 + x2*w2
    if t <= θ
        return 0
    elseif t > θ
        return 1
    end
end

println(OR(0,0))    # 0
println(OR(0,1))    # 1
println(OR(1,0))    # 1
println(OR(1,1))    # 1


function NOT(x)
    w = 0.5
    θ = 0.25
    t = x * w
    if t <= θ
        return 1
    elseif t > θ
        return 0
    end
end

println(NOT(0))     # 1
println(NOT(1))     # 0

function NAND(x1,x2)
    w1 = -0.5
    w2 = -0.5
    θ  = -0.75
    t  = x1*w1 + x2*w2
    if t <= θ
        return 0
    elseif t > θ
        return 1
    end
end

println(NAND(0,0))  # 1
println(NAND(0,1))  # 1
println(NAND(1,0))  # 1
println(NAND(1,1))  # 0

function XOR(x1,x2)
    α1 = NAND(x1,x2)
    α2 = OR(x1,x2)
    β  = AND(α1,α2)
    return β
end

println(XOR(0,0))   # 0
println(XOR(0,1))   # 1
println(XOR(1,0))   # 1
println(XOR(1,1))   # 0