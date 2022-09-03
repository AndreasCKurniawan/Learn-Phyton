# ACCESSS ITEMS
# List items are indexed and you can access them by referring to the index number:

list = ['apple', 'watermelon', 'melon', "grape", 'tomato', 'cabbage']
print(list[0])

# NEGATIVE INDEX
# it will access from last item
print(list[-1])

# RANGE OF INDEX
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
print(list[1:3])

# By leaving out the start value, the range will start at the first item:
print(list[:3])

# By leaving out the end value, the range will go on to the end of the list:
print(list[4:])

# RANGE OF NEGATIVE INDEXES
# Specify negative indexes if you want to start the search from the end of the list:

print(list[-4:-1])

# CHECK IF ITEM EXIST
# To determine if a specified item is present in a list use the in keyword:
print('watermelon' in list)
