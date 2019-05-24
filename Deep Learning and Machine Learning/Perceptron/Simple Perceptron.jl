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