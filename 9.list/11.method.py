# LIST METHOD

list = ['apple', 'banana', 'cherry']
print('Starter list\n', list)

# .append()
# add element at the end
list2 = list.copy()
list2.append('Brick')
print('# append()')
print(list2)
list2.pop()

# .clear()
# removes all element from list
list2.clear()
print('# .clear()')
print(list2)

# .copy()
# return a copy of a list
list2 = list.copy()
print("# copy")
print(list2)

# .count()
# return total items with specified value in a list
print('# .count()')
print(list2.count("banana"))

# .extend()
# Add the elements of a list (or any iterable), to the end of the current list
print("# .extend()")
list2.extend('test')
list2.extend(list)
print(list2)

list2 = list.copy()

# .index()
# return index of first element with specified value
print('# .index()')
print(list2.index('banana'))

# .insert()
# add items into spesified position in list
print('# .insert()')
print(list2)
list2.insert(2, "Mouse")
print(list2)

# .pop()
# remove items at specified position / end if not given position
list2.pop(2)
print("# .pop()")
print(list2)

# .remove()
# remove items with specified value
print('# .remove()')
list2.remove('apple')
print(list2)

# .reverse()
# reverse the order of list
list2.reverse()
print('# .reverse()')
print(list2)

# .sort()
# sort the item list
list2.sort()
print('# .sort()')
print(list2)
