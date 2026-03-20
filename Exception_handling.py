# Exception Handling
# Exception Handling is a way to protect your program from crashing when an error occurs.

# Types of Exceptions:
# 1. ZeroDivisionError
# 2. ValueError
# 3. TypeError
# 4. IndexError
# 5. KeyError
# 6. AttributeError
# 7. FileNotFoundError
# 8. ImportError
# 9. NameError
# 10. SyntaxError
"""
Python uses:
1.try : check code
2.except : handle errors
3.else : execute if no error
4.finally : always execute
"""

# ✅ Basic Structure
# try:
#     # Code that may raise an exception
# except SomeError:
#     # What to do if error happens
# else:
#     # Run if no error
# finally:
#     # Always run (cleanup, close file, etc.)

# try-except Block
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Error occurred")

try:
    a = int(input())
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# else Block
try:
    a = int(input())
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No error occurred")
finally:
    print("Always runs")


# finally Block
try:
    a=int(input("enter a number :"))
    print(a)
except Exception as e:
    print("invalid input",e)
    print(f"invalid input {e}")
finally:
    print("always runs")

try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("Execution completed")

# Raising Exceptions
try:
    raise ValueError("Custom error message")
except ValueError as e:
    print("Caught:", e)

age = int(input())
if age < 18:
    raise Exception("Not eligible")


# Custom Exception
class MyError(Exception):
    pass
try:
    raise MyError("Custom error")
except MyError as e:
    print(e)

#Most IMP example in Exception Handling
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)
finally:
    print("Always runs")


try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result:", result)
finally:
    print("Program ended")


try:
    a=input("enter a name: ").lower()
    if a !="abhi":
        raise Exception("you only marry abhi..")
except Exception as e:
    print("Error : ",e)
else:
    print("I'm ready to marry")
finally:
    print("Abhi is right person to marry Raddy")