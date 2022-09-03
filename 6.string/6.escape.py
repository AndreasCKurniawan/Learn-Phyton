# ESCAPE CHARACTER USING '\'
txt = "We are the so-called \"Viking\" from the north."
# \' -> single quote
# \\ -> backslash
# \n -> new line
# \r -> Carriage Return
txt = "test \r test"
print(txt)
# \t -> Tab
txt = "test \t test"
print(txt)
# \b -> backspace
txt = "test \b test"
print(txt)
# \f -> form feed
txt = "test \f test"
print(txt)
# \ooo -> octal value
txt = "test \ooo test"
print(txt)
# \xhh -> hex value
