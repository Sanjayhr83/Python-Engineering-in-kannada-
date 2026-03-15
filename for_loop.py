#for loop(In Python, a for loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code repeatedly for each element in the sequence.)
# for item in sequence:
    # Code to execute for each item in the sequence

for i in range(10):
    print(i,end=" ")

cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)

z=["a","b","c","d"]
for alpha in z:
    print(alpha)

for i in range(1,100,5):#range(start,stop,step)
    print(i,end=" ")

name="RahulMadhi"
for index,i in enumerate(name):
    print(i*(index+1))


#Multiplication Table
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print(" ")# To print an empty line after each table
for i in range(1,11):
    print(f"2X{i}={2*i}")

# Using break in a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)

#Using continue in a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        continue
    print(city)


#Looping Through a List with enumerate()
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")

#Using else with for Loops
for city in cities:
    print(city)
else:
    print("No more cities!")

#Count Vowels in a String:(Write a program that counts how many vowels are in a given string using a for loop.)
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)


#total count
l=[1,2,34,56,75,32,94]
print(l)
total=0
for num in l:
    print(total)
    total+=num
print("Total:", total)

#Looping Through Lists
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("Total sum:", total)

numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print("Doubled List:", doubled)


#Looping Through Dictionaries
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}
for student in student_marks:
    print(student)

student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}
for marks in student_marks.values():
    print(marks)

#for Loops with range()
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]
student_marks = {}
for i in range(len(students)):
    student_marks[students[i]] = marks[i]
print(student_marks)
