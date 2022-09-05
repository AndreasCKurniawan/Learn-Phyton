from mymodule import person1
import platform
import mymodule as mx
import mymodule

mymodule.greeting('jonathan')

# ACCESS MODEL VAIRABLE
x = mymodule.person1['age']
print(x)

# RENAMING A MODEL
a = mx.person1['country']
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

x = dir(platform)
print(x)

# import from module

print(person1["age"])
