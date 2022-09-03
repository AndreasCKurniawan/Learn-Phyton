list = ['apple', 'watermelon', 'melon', "grape", 'tomato', 'cabbage']

# ADD LIST ITEMS

# APPEND ITEMS
# to add new item to end of the list use '.append()'
print(list)
list.append("smartphone")
print(list)

# INSERT ITEMS
# to add into spesifix index use '.insert()'
list.insert(0, 'table')

# EXTEND LIST
# to append elements from another list us 'extend()'
list2 = ['black', 'gray', 'white']
list.extend(list2)
print(list)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
tuple = ('wood', 'metal')
list.extend(tuple)
print(list)
