# GLOBAL VARIABLE
# variable that are created outside a function are known as global variables
# global variable can be used by everyone, both inside of function and outside

x = "awesome"


def myFunct():
    print("Phyton is " + x)


myFunct()

# You can create local variable by puting 'global' keyword


def myFunct2():
    global a
    a = "Fantastic"
    print("Local Variable " + a)


myFunct2()


print('Global Variable ' + a)
