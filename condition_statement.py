#if,elif,else

#signal light example
signal="red"
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready to go")
elif signal=="green":
    print("go safely")
else:
    print("nothing happen")

# Let's extend the dinner example by adding an alternative action if it's not 8 PM.
time = 15  # 3 PM
if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")

#college attendence example
a=35
is_teacher_friend=True
if a>=85:
    print("able to attend the exam")
elif a<75 and is_teacher_friend:
    print("not able to attend the exam")
else:
    print("not sure")


#Checking Bus Ticket Prices
gender=input("enter the gender : ")
age=int(input("enter the age : "))

if gender=="female":
    print("ticket is free")
else:
    if gender=="male" and (age>=18 and age<=59):
        print("pay full amount")
    elif gender=="male" and age>=60:
        print("senior citizen discount")
    elif gender=="male" and age<=7:
        print("child discount")
    else:
        print("enter invalid")

#Indentation in Python
age = 19
if age >= 18:
    print("You are eligible to vote.")
    print("Remember to bring your voter ID.")
else:
    print("You are not eligible to vote.")


#Nested if Statements
day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")

#The match-case Statement (Python 3.10+)
day = input("enter week day : ")
match day:
    case "monday":
        print("Start of the work week.")
    case "friday":
        print("Almost weekend!")
    case "saturday" | "sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")
