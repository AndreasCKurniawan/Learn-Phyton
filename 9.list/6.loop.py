# LOOP THROUGHT LIST

list = ['apple', 'watermelon', 'melon', "grape", 'tomato', 'cabbage']

# for
for x in list:
    print('for loop', x)

# INDEX NUMBER
for i in range(len(list)):
    print('index ', list[i])

# WHILE LOOP
i = 0
while i < len(list):
    print('while ', list[i])
    i = i + 1

# USING LIST COMPREHENSION
[print(x) for x in list]
