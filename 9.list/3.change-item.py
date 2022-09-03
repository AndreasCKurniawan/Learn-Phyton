# CHANGE LIST ITEM
list = ['apple', 'watermelon', 'melon', "grape", 'tomato', 'cabbage']
print(list)

list[0] = "chips"
print(list)

# CHANGE RANGE ITEM VALUES
list[1:4] = ['chili', 'pepper']
print(list)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
list[1:5] = ['chili']
print(list)

# INSERT ITEM
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
list.insert(0, "mouse")
print(list)
