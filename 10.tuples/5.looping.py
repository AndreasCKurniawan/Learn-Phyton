import this


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


# INDEX
for i in range(len(thistuple)):
    print(thistuple[i])
    i = i+1

# WHILE
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
