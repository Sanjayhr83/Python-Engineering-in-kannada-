"""
The match-case Statement (Python 3.10+)
Starting from Python 3.10, you can use the match-case statement for pattern matching—similar to switch-case in other languages like C or JavaScript. It helps you write cleaner and more readable code when checking a variable against multiple constant values.

Syntax:
match variable:
    case value1:
        # Code block for value1
    case value2:
        # Code block for value2
    case _:
        # Default case (like else)
"""

day = "Sunday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")



num= int(input("Num: "))
match num:
    case 1:
        print("num is equal to one")
    case 2:
        print("num is equal to two")
    case 3:
        print("num is equal to three")
    case 4:
        print("num is equal to four")
    case 5:
        print("num is equal to five")
    case _:
        print("Invalid input")


time=int(input("enter time: "))
match time:
    case 8:
        print("Breakfast time")
    case 1:
        print("Lunch time")
    case 7:
        print("Dinnertime")
    case 5:
        print("Snacks time ")
    case _:
        print("invalid input")