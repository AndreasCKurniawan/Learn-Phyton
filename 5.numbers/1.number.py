# PHYTON NUMBER
# - INT
#   whole number, positive or negative. without decimal of unlimited length
# - FLOAT
#   'floating point number' is a number that containing one or more decimal
#   float can contain 'e' to indicate the power of 10
# - COMPLEX
#   complex numbers are written with a 'j' as the imaginary part

# TYPE CONVERSION
import random
x = 1
y = 2.8
z = 1j

a = float(x)
b = complex(y)
print(a, b, )
# c = int(z)
# you cant convert complex into another number

# RANDOM NUMBER
# phyton doesn't have a random function
# you should import hte built in module called 'random'
print(random.randrange(0, 10))
