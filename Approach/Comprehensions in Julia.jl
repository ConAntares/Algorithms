#### Comprehensions

re = [i for i in 1:10]
println(re)              
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

re = [i*j for i in 1:4, j in 2:5]
println(re)
    # [2  3  4  5; 
    #  4  6  8 10; 
    #  6  9 12 15; 
    #  8 12 16 20]

re = [i*j+k for i in 1:4, j in 2:5, k in 2:4]
println(re)
    # [ 4  5  6  7; 
    #   6  8 10 12; 
    #   8 11 14 17; 
    #  10 14 18 22]

    # [ 5  6  7  8; 
    #   7  9 11 13; 
    #   9 12 15 18; 
    #  11 15 19 23]

    # [ 6  7  8  9; 
    #   8 10 12 14; 
    #  10 13 16 19; 
    #  12 16 20 24]

re = [i for i in 1:10 if i % 2 == 0]
println(re)
    # [2, 4, 6, 8, 10]

# Set