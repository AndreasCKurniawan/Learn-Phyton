# list are use to store multiple value in one variable
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# lists created using square bracket []

list = ['apple', 'banana', 'cherry']
print(list)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# ORDERED
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# CHANGEABLE
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# ALLOW DUPLICATE
# Since lists are indexed, lists can have items with the same value:
list = ['apple', 'apple', 'apple']
print(list)

# LIST LENGTH
# we can use len(_list_) to count the length of list
print(len(list))


# LIST DATA TYPES
# List items can be of any data type:
list1 = ["apple", "banana"]
list2 = [1, 2, 3]
list3 = [True, False, True]
# A list can contain different data types:
list4 = ['apple', 1, True]

# list() CONSTRUCTOR
# It is also possible to use the list() constructor when creating a new list.
# myList = list("apple", "banana", "cherry")
# print(myList)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
