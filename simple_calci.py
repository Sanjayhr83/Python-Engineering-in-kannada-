"""Menu-Driven Programs in Python
A menu-driven program is a program that allows users to interact by choosing options from a menu.
These programs are commonly used in applications such as banking systems, shopping carts, or command-line utilities.
Menu-driven programs are typically implemented using loops and conditional statements (if-elif-else).

Steps to Create a Menu-Driven Program
1. Display the Menu: Use print() statements to display a list of options.
2. Take User Input: Use input() to capture the user's choice.
3. Process the Choice: Use conditional statements to execute actions based on the user's input.
4. Repeat Until Exit: Use a loop (while) to keep displaying the menu until the user chooses to exit.
"""

# Basic Structure of a Menu-Driven Program

# def menu():
#     print("Welcome to the Menu-Driven Program!")
#     print("1. Option 1")
#     print("2. Option 2")
#     print("3. Option 3")
#     print("4. Exit")

# while True:
#     menu()
#     choice = input("Enter your choice (1-4): ")
    
#     if choice == '1':
#         print("You selected Option 1.")
#     elif choice == '2':
#         print("You selected Option 2.")
#     elif choice == '3':
#         print("You selected Option 3.")
#     elif choice == '4':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# Scenario: Simple Calculator
# A menu-driven program to perform basic arithmetic operations.

def menu():
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice in ['1', '2', '3', '4']:
        # Get two numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")


#Banking System
def Menu():
    print("Banking System")
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Exit")

balance= 5000

while True:
    Menu()
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        print(f"Your balance is {balance}")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Your balance is {balance}")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Your balance is {balance}")
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")


#Grocery Store Menu:
def Menu():
    print("Shopping System")
    print("1. Add items to their cart")
    print("2. Rmove items")
    print("3. View the total price")
    print("4. Exit")

while True:
    Menu()
    choice= int(input("Enter your choice 1-4: "))

    if choice==1:
        a=input("enter your items : ")
        print("Yours items are add to your cart..")
    elif choice ==2:
        b=input("enter your items : ")
        print("Remove Your items from your cart..")
    elif choice==3:
        c=2893
        print("Your total ammount is ",c)
    elif choice==4:
        print("You are choice exit and Thank you for shopping...")
        break
    else:
        print("Invalid input...")


#Educational System:
def Menu():
    print("\n Educational System")
    print("1. Add student deatils")
    print("2. Display students deatils")
    print("3. Exit")

while True:
    Menu()
    choice=int(input("Enter your choice 1-3 : "))
    if choice==1:
        a=input("Enter student deatils : ")
        print("I accept student details")
    elif choice==2:
        print("Student deatils is",a)
    elif choice==3:
        print("You are choice exit, GOODBYEE....!!")
        break
    else:
        print("Invalid input...")
