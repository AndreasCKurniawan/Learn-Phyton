# LIST COMPREHENSION
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# WITHOUT COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# WITH COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# SYNTAX
# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# IRETABLE
# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10) if x > 0]
print(newlist)

# EXPRESSION
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]
print(newlist)
