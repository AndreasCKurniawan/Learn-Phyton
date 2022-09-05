# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
x = thisdict.get('year')
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# GET VALUES
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)

# GET ITEM
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
if "brand" in thisdict:
    print(True)
