# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.discard("banana")
print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
thisset.pop()
print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:

# del keyword will delete set complety
