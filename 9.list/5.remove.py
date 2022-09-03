list = ['apple', 'watermelon', 'melon', "grape", 'tomato', 'cabbage']
print(list)

# REMOVE LIST ITEMS

# REMOVE SPESIFIC ITEM
# '.remove()' method removes the specified item
list.remove('apple')
print(list)

# REMOVE SPECIFIED INDEX
# .pop() / del _list_
list.pop(-1)  # or list.pop() to remove last item
print(list)

del list[-1]
print(list)

# delete entire list
del list
print(list)

# CLEAR LIST
# .clear() = empty the list
# list.clear()
# del list[:]
# print(list)
