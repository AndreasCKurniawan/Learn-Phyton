# UPDATE TUPLES
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.

# CONVERT INTO LIST
tuple1 = ('samsung', 'apple', 'nokia')
tupleList = list(tuple1)
tupleList.append('xiaomi')
print(tupleList)
tuple1 = tuple(tupleList)
print(tuple1)

# ADD TUPLE A TUPLE
# You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
tuple1 += ("realme",)
print(tuple1)

# REMOVE ITEM
# CHAGE IT TO LIST FIRST, THEN DELETE DATA. AFTER THAT CHANGE IT BACK TO TUPLE
# or delete all tuple
del tuple1

print(tuple1)  # error because tuple no longer exist
