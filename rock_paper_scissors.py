import random
choices= ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter your choice: ").lower()

print("Computer choice: ", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user == "scissors":
    if computer == "paper":
        print("You win!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")

