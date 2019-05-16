#### Format

str = "{0} love {1}.{2}".format("I", "FishC", "com")
print(str)                              # I love FishC.com

str = "{a} love {b}.{c}".format(a="I", b="FishC", c="com")
print(str)                              # I love FishC.com

str = "{0} love {a}.{b}".format("I", a="FishC", b="com")
print(str)                              # I love FishC.com

str = "{0:.1f}{1}".format(27.658," GB")
print(str)                              # 27.7 GB

## String Format Operator 
"""
%c      Format string and ASCII number
%s      Format string
%d      Format integer
%o      Format unsigned octal number
%x      Format unsigned hexadecimal number
%X      Format unsigned hexadecimal number in capital form
%f      Format float
%e      Format float with scientific notation single e
%E      Format float with scientific notation single E
%g      Format float into %f or %e depend the value of number
%G      Format float into %f or %e depend the value of number 
"""

print("%c" % 97)                        # a
print("%c %c %c %c" % (97,98,99,100))   # a b c d
print("%s" % "Hello World")             # Hello World
print("%d + %d = %d" % (4,5,4+5))       # 4 + 5 = 9
print("%o" % 9)                         # 11
print("%x" % 12)                        # c
print("%X" % 12)                        # C
print("%f" % 1.23456)                   # 1.234560
print("%e" % 1.23456)                   # 1.234560e+00
print("%E" % 1.23456)                   # 1.234560E+00
print("%g" % 1.23456)                   # 1.23456
print("%G" % 1.23456)                   # 1.23456

## Auxiliary Command for String Format
"""
m.n     m: Minimum width, n: Digits
-       Left justifying
+       Display the sign of positive number
0       Fill with 0
#o      Display the sign of Octal(0o) 
#x      and Hexadecimal with 0x
#X      and Hexadecimal with 0X
"""

print("%17.16f" % 1.234567890123456789) # 1.2345678901234567
print("%17.14f" % 1.234567890123456789) # 1.23456789012346
print("%17.12f" % 1.234567890123456789) # 1.234567890123
print("%+17.8f" % 1.234567890123456789) # +1.23456789
print("%0d"     % 123456)               # 123456
print("%010d"   % 123456)               # 0000123456
print("%#o"     % 123456)               # 0o361100
print("%#x"     % 123456)               # 0x1e240
print("%#X"     % 123456)               # 0X1E240
print("%#d"     % 0x1e240)              # 123456

## Escape Character
# \"      "
# \"      "
# \\      \
# \a      Make a sound
# \b      Backspace character
# \n      Newline character
# \t      Horizontal tab character (Table)
# \v      Vertical tab character
# \r      Enter character
# \f      Newpage character
# \o      Octal character
# \x      Hexadecimal character
# \0      Empty character

print("Hello, world! \nHello, Python!")