# SORT LIST

# ASC
list = ['apple', 'watermelon', 'melon', "grape", 'tomato', 'cabbage']
print(list)

list.sort()
print(list)

# DESC
list.sort(reverse=True)
print(list)

# CUSTOM


def sortFunc(n):
    return abs(n-50)


list2 = [100, 200, 59, 1]
print(list2)

list2.sort(key=sortFunc)
print(list2)

# CASE INSENSITIVE
# list will make capital letter first
list3 = ["andreas", "caesar", 'Kurniawan']
list3.sort()
print(list3)

list3.sort(key=str.lower)
print(list3)

# REVERSE
list3.reverse()
print(list3)
