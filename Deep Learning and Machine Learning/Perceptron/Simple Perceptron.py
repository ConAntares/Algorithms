#### Simple Perceptron

# 1.Received an AND function with parameters (x1, x2)
def AND(x1,x2):
    w1 = 0.5
    w2 = 0.5
    θ  = 0.7
    t  = x1*w1 + x2*w2
    if t <= θ:
        return 0
    elif t > θ:
        return 1

print(AND(0,0))     # 0
print(AND(0,1))     # 0
print(AND(1,0))     # 0
print(AND(1,1))     # 1