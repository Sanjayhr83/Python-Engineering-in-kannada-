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
