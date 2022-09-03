# STRING FORMAT
# because we cant combine string with number, but we can combine by using format method

# USE FORMAT TO INSERT INTO STRING


txt = "my name is john, and im {}"
print(txt.format(20))

# MULTIPLE ARGUMENT
TXT = "MY NAME IS {}, AND IM {}"
print(TXT.format('ANDREAS', 20))

# USING INDEX NUMBER TO CHANGE POSITION
total = 5
itemName = "aowkda"
price = 5000
txt = "Harga {1}, total item {2}, nama item {0}"
hasil = txt.format(itemName, price, total)
print(hasil)
