# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime as date

x = date.datetime.now()
print(x)
print('year', x.year)
print(x.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
x = date.datetime(2002, 4, 2)
print(x.strftime('%A'))
