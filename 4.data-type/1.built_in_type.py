# TODO BUILT IN DATA TYPE
# Text type       : str
# Numeric Types   : int, float, complex
# Sequence Types  : list, tuple, range
# Mapping Type    : dict
# Set Types       : set, frozenset
# Boolean Stpe    : bool
# Binray Types    : bytes, bytearray, memoryview
# None Type       : NoneType
# #

# Getting the Data Type
x = 5
print(type(x))

# SETTING DATA TYPE
x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ['apple', 'banana', 'cherry']
print(type(x))

x = ('apple', 'banana', 'cherry')
print(type(x))

x = range(5)
print(type(x))

x = {'name': 'John', 'age': 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))
