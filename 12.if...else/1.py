if 2 > 1:
    print('2')
elif (2 < 1):
    print("1")
else:
    print('0')

# SHORTHAND
# if a > b: print("a is greater than b")

# IFELSE
# print("A") if a > b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
    pass
