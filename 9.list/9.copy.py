# COPY LIST
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().

list = [1, 2, 3, 4, 5]
list2 = list
print(list2)

list[0] = 100
print(list2)

list2 = list.copy()
print(list2)

list0 = [1]
print(list2)

# Another way to make a copy is to use the built-in method list().
# thisList = [1, 2, 3, 4, 5]

# list4 = list(thisList)
# print(list4)
