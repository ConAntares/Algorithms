####  Logical Symbol

## And: &
str = false & false
println(str)            # false

str = false & true
println(str)            # false

str = true & false
println(str)            # false

str = true & true
println(str)            # true

str = false & missing
println(str)            # false

str = true & missing
println(str)            # missing

## Or: |
str = false | false
println(str)            # false

str = false | true
println(str)            # true

str = true | false
println(str)            # true

str = true | true
println(str)            # true

str = false | missing
println(str)            # missing

str = true | missing
println(str)            # true

## Not: ~
str = ~ true
println(str)            # false

str = ~ false
println(str)            # true

str = ~ missing
println(str)            # missing

## Nand
str = ~(false & false) 
println(str)            # true

str = ~(false & true) 
println(str)            # true

str = ~(true & false) 
println(str)            # true

str = ~(true & true) 
println(str)            # false

str = ~(false & missing) 
println(str)            # true

str = ~(true & missing) 
println(str)            # missing

# Nor
str = ~(false | false) 
println(str)              # true

str = ~(false | true) 
println(str)              # false

str = ~(true | false) 
println(str)              # false

str = ~(true | true) 
println(str)              # false

str = ~(false | missing) 
println(str)              # missing

str = ~(true | missing) 
println(str)              # false

## Xor
str = xor(false, false)
println(str)            # false

str = xor(false, true)
println(str)            # true

str = xor(true, false)
println(str)            # true

str = xor(true, true)
println(str)            # false

str = xor(false, missing)
println(str)            # missing

str = xor(true, missing)
println(str)            # missing