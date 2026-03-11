single='single quote string'
double="double quote string"
triple="""triple quote string"""

print(single)
print(double)
print(triple)

#string concatenation
x="abhi"
y="rathod"
print(x + " " + y)

warning="Warning !!!"*5
print(warning)

#string methods
case="  MMBenal is ours principle  "
print(case.upper()) #converts to uppercase
print(case.lower()) #converts to lowercase
print(case.isupper()) #checks if the string is uppercase
print(case.islower()) #checks if the string is lowercase
print(case.startswith("M")) #checks if the string starts with the given character
print(case.endswith("l")) #checks if the string ends with the given character
print(case.find("a")) #finds the index of the given character
print(case.capitalize()) #converts the first character to uppercase
print(case.title()) #converts the first character of each word to uppercase
print(case.strip()) #removes whitespace from the beginning and end
print(case.replace("principle", "head")) #replaces the given character with another character
print(case.split(" ")) #splits the string into a list
print(len(case)) #returns the length of the string

#string formating
Name="ravi"
age=23
print("my name is",Name,"and my age is",age)
print("My name is {} and my age is {}".format(Name,age))
print(f"My name is {Name} and my age is {age}")

#string indexing(it is depends on step value)
string="PentagonSpace"
print(string[0])    #P
print(string[1:11:2]) #entgn
print(string[::-1]) #ecapSnoitagonP([start:stop:step])
print(string[-1]) #e
print(string[-2]) #c
print(string[0:9:-1]) #empty string([start:stop:step])
