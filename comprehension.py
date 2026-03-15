#List Comprehension(List comprehension provides a more concise way to create lists by applying an expression to each element in an existing list.
#new_list = [expression for item in iterable if condition]
print("list comprehension :")
l=[x for x in range(1,21)]
dl=[x**2 for x in l]
print(l)
print(dl)
edl=[x**2 for x in l if x%2==0]
print(edl)

#Squaring numbers in a list
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

#Filtering even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squares)

#Uppercasing Kannada city names
cities = ['bangalore', 'mysore', 'hubballi', 'mangalore', 'belagavi']
upper_cities = [city.upper() for city in cities]
print(upper_cities)

#Dictionary Comprehension(Similar to list comprehension, dictionary comprehension provides a concise way to create dictionaries.)
#new_dict = {key_expression: value_expression for item in iterable if condition}

print("dictionary comprehension :")
# Creating a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)

#Converting a list of names to a dictionary of name lengths
names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

#Filtering cities with population above 10 lakhs (Localized Example)
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)


#Splitting Strings to Create Lists
#syntax :   string.split(separator, maxsplit)

print("spliting string to create lists:")
#Splitting a sentence into words
sentence = "I love coding in Python"
words = sentence.split()
print(words)

# Splitting a string with commas
data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)

#Limiting the number of splits
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)
