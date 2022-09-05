# ADD DICTIONARY ITEM

# ADDING ITEMS
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

from tkinter import X


x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x['color'] = 'black'
print(x)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.

x.update({'tire_color': 'white'})
print(X)
