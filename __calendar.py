#static method 
import calendar

year = 2026
month = 9

print(calendar.month(year,month))


#dynamic method
import calendar

year = int(input("Enter year : "))
month = int(input("Enter month (1-12) : "))

print(calendar.month(year,month))

