#### N-ary Arrangement

# Input a Vector as Sequence:
A = [2,4,3,1]
println("The sequence is ",A)
# Print the elements number of the Vector:
println("The number of elements is ",length(A))
# Initialize the Order Number:
o = Int64(0)
# Initialize the Reverse Order Number:
t = Int64(0)

# Calculus the Order Number and the Reverse Order Number:
for i in 1:length(A)
    for j in 1:(i-1)
        # print(i,",",j,";")
        if A[j] < A[i]
            global o = o + 1
        elseif A[j] > A[i]
            global t = t + 1
        end
    end
end
println("The Order Number of this Sequence is: ",o)
println("The Reverse Order Number of this Sequence is: ",t)

# Determine whether the sequence is odd or even:
if rem(0,2) == 0
    println("This Sequence is even.")
elseif  rem(0,1) == 0
    println("This Sequence is odd.")
end