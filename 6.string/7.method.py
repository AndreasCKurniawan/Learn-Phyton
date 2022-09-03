from cgi import print_arguments
from cmath import pi
from xmlrpc.server import list_public_methods


t = "test test test"
# capitalize()
# turn first character to uppercase
print("# .capitalize()")
print(t.capitalize())

# .casefold()
# convert string into lower case


def casefoldFuncion():
    txt = "TEST TEST TEST"
    print("# .casefold()")
    print(txt.casefold())


casefoldFuncion()

# .center(_length_, _char_{optional})
# return a centered string with lenght side
print("# .center()")
print(t.center(50, "a"))

# .count(_string_)
# return number of times a specified value occurs in a string
print("# .count()")
print(t.count("test"))

# .encode()
# return an encoded varsion of string
print("# .encode(_string_)")
print(t.encode())

# .endswitch()
# returns true if the string end with the specified value
print("# .endswitch()")
print(t.endswith('test'))

# .expandtabs()
# set thetab size of string
print("# .expandtabs(_int_)")
txt = "test \t test"
print(txt.expandtabs(100))

# .find(_string_)
# search the string and return the first position founded

print("# .print(_string_)")
print(t.find("st"))

# .format(arg1, arg2, ...)
# .format specified value in a string
txt = "value 1 : {}, value 2 : {}"
print("# .format()")
print(txt.format("a", "b"))

# .index(_string_)
# search the string and return the first position founded
print("# .index()")
print(t.index("test"))

# .isalnum()
# return true if all char are alphanumeric (a-z) & (0-9)
print('# isalnum')
txt = "12a"
print(txt.isalnum())

# .isalpha()
# return true if characters in string are alphabet (a-z)
txt = "abc"
print("# .isalpha()")
print(txt.isalpha())

# .isdecimal()
# return true if all character unicode are deciman
txt = "\u0030"
print('# .isdecimal()')
print(txt.isdecimal(), txt)

# .isdigit()
# return true if all character all digit
txt = '12345'
print("# isdigit()")
print(txt.isdigit())

# .isidentifier()
# return true if string is valid identifier
txt = "2Demo"
print("# .isidentifier()")
print(txt.isidentifier())

# .islower()
# return true if all character are lowercase
txt = "Test"
print("# .islower()")
print(txt.islower())

# .isnumeric
# return true if all char are numeric ( - and . not a numeric)
print("# .isnumeric")
txt = "123"
print(txt.isnumeric())
txt = "-112#3"
print(txt.isnumeric())


# .isprintable()
# return true if all character are printable
print('# .isprintabel()')
print(txt.isprintable())

# .isspace()
# return true if all char are whitespaces
txt = "   5   "
print("# .isprintable()")
print(txt.isspace())  # false
txt = "      "
print(txt.isspace())  # true

# .istitle()
# return true if string follow ther rules of title
# ( all words start with a uppercase and rest lower case)
txt = "Andreas Caesar"
print("# .istitle()")
print(txt.istitle())
txt = "andReas caesar"
print(txt.istitle())

# .isupper()
# return true if all chars is a uppercase
txt = "ANDREAS"
print("# .isupper()")
print(txt.isupper())

# _string_.join(_variable_)
# join iratable with string between
myTupple = ("john", "peter", "vicky")
print("# .join(_string_)")
print(" joined ".join(myTupple))

# .lower()
# convert string into lowercase
print("# .lower()")
print(txt.lower())
# .upper()
# conver string into uppercase
print(txt.upper())

# todo ??? lstrip()
# ????

# .maketrans(_string_, _string_)
# .return dict of a translation string
# .translate()
# return converted versiton of translation dict string
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(mytable)
print(txt.translate(mytable))

# .partition(_string_)
# Search for the word first "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all bananas day"
x = txt.partition("bananas")
print('# .partition()')
print(x)
print('# .rpartition()')
# search for the last word
x = txt.rpartition("bananas")
print(x)


# .replace(_string_, _string_)
x = txt.replace("banana", "apple")
print("# .replace()")
print(x)

# .rfind(_string_)
# find string and return last word position it find
print("# .rfind()")
txt = "banana banana"
print(txt.find('banana'))
print(txt.rfind('banana'))

# .rindex()
# find string and return last word position it find
print("# .rindex()")
print(txt.index("banana"))
print(txt.rindex("banana"))

# .rjust(_int_)
# add space * int at right of the text
print(txt.rjust(100), "Test")
# .ljust(_int_)
# add space * int at left of the text
print(txt.ljust(100), "Test")

# .rsplit() & split()
# separate work using spesific word and return it as a list
rsplit = txt.rsplit(" ")
print("# .rsplit() & .split()")
print(rsplit)
split = txt.split(" ")
print(split)

# .splitlines()
# separate word using newline (\n) as separator
txt = "test \n test"
print("# .splitlines()")
print(txt.splitlines())

# .startwith(_string_)
# return true if string start with that value
txt = "testing data"
print("# .startwith()")
print(txt.startswith('test'))

# .strip()
# return a trimmed version of string
print("# .strip()")
txt = "     banana     "
x = txt.strip()
print(x)

# .swapcase()
# change from lowercase to uppercase and the opposite
txt = "Andreas Kurniawan"
print("# .swapcase()")
print(txt.swapcase())

# .title()
# convert first character of each word into uppercase
txt = "andreas kurniawan"
print("# .title()")
print(txt.title())
