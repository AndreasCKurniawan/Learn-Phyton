tuple_ = ('apple', 'banana', 'cherry')

# A tuple is a collection which is ordered and unchangeable.
# tuple written in with round brackets
print(tuple_)

# TUPLE ITEMS
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# UNCHANGEABLE
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# ALLOW DUPLICATES
# Since tuples are indexed, they can have items with the same value:
tuple2 = ("apple", "banana", "cherry", "apple", "cherry")

# TUPLE LENGTH
print(len(tuple_))

# CREATE TUPLE WITH ONE ITEM
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tuple2 = ('Test')
print(tuple2)
tuple2 = ('Test',)
print(tuple2)

# TUPLE DATA TYPES
# Tuple items can be of any data type:

# tuple() CONSTRUCTOR
tuple5 = tuple(('data1', 'data2'))
print(tuple5)
