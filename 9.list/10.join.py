# JOIN LIST
list = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# using + operator
list3 = list + list2
print(list3)

# appending one by one
for x in list2:
    list.append(x)

print(list)

# using extend()
list3.extend(list)
print(list3)
