####  Logical Symbol

## And
str = False and False
print(str)              # False

str = False and True
print(str)              # False

str = True and False
print(str)              # False

str = True and True
print(str)              # True

## Or
str = False or False
print(str)              # False

str = False or True
print(str)              # True

str = True or False
print(str)              # True

str = True or True
print(str)              # True

## Not
str = not True
print(str)              # False

str = not False
print(str)              # True

## Nand
str = not (False and False) 
print(str)              # True

str = not (False and True) 
print(str)              # True

str = not (True and False) 
print(str)              # True

str = not (True and True) 
print(str)              # False

## Nor
str = not (False or False) 
print(str)              # True

str = not (False or True) 
print(str)              # False

str = not (True or False) 
print(str)              # False

str = not (True or True) 
print(str)              # False

## Xor
str = (not (False and False)) and (False or False)
print(str)              # False

str = (not (False and True)) and (False or True)
print(str)              # True

str = (not (True and False)) and (True or False)
print(str)              # True

str = (not (True and True)) and (True or True)
print(str)              # False