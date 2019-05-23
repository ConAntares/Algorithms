#### Simple Perceptron with Weight and Bias

using LinearAlgebra

x = [0.0, 1.0]
w = [0.5, 0.5]
b = -0.75

re = .*(w,x)
println(re)
    # [0.0, 0.5]
re = sum(w.*x) + b
println(re)
    # -0.25

function AND(x1,x2)
    x = [x1, x2]
    w = [0.5,0.5]
    b = -0.75
    t = sum(w.*x) + b
    if t <= 0
        return 0
    else
        return 1
    end
end

println(AND(0,0))   # 0
println(AND(0,1))   # 0
println(AND(1,0))   # 0
println(AND(1,1))   # 1

function OR(x1,x2)
    x = [x1, x2]
    w = [0.5,0.5]
    b = -0.25
    t = sum(w.*x) + b
    if t <= 0
        return 0
    else
        return 1
    end
end

println(OR(0,0))    # 0
println(OR(0,1))    # 1
println(OR(1,0))    # 1
println(OR(1,1))    # 1

function NAND(x1,x2)
    x = [x1, x2]
    w = [-0.5,-0.5]
    b = 0.75
    t = sum(w.*x) + b
    if t <= 0
        return 0
    else
        return 1
    end
end

println(NAND(0,0))  # 1
println(NAND(0,1))  # 1
println(NAND(1,0))  # 1
println(NAND(1,1))  # 0

## XOR: A simple 2-layered perceptron
function XOR(x1,x2)
    α1 = NAND(x1,x2)
    α2 = OR(x1,x2)
    β  = AND(α1,α2)
    return β
end

println(XOR(0,0))     # 0
println(XOR(0,1))     # 1
println(XOR(1,0))     # 1
println(XOR(1,1))     # 0