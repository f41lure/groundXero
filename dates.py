from datetime import *

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

date1 = date(year, month, day)

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

date2 = date(year, month, day)

d = date1 - date2

print(d)
