#constructor:It allows you to set the initial state of the object by defining its attributes.
#The __init__() method in Python is a special method that initializes an object when it’s created. It’s called automatically when you create a new instance of a class.
# class ClassName:
#     def __init__(self, parameter1, parameter2):
#         self.attribute1 = parameter1
#         self.attribute2 = parameter2

# Using self in Class Methods
# self: Refers to the instance of the class itself, allowing you to access attributes and methods within a class.
# It is automatically passed as the first argument to methods within the class.
# Note: While self is a convention, you can technically use any name (though it's not recommended for readability).

class Person:
    def __init__(self, name, age):
        self.name = name  # 'self.name' is an instance variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Arjun", 22)
person1.introduce()
person2=Person("Abhishek",23)#creating another object
person2.introduce() #calling method
print(person2.name) #Accessing the name attribute
print(person2.age) #Accessing the age attribute


# Creating Multiple Objects with Different Attributes
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

laptop1 = Laptop("Dell", 45000)
laptop2 = Laptop("HP", 55000)

laptop1.show_info()
laptop2.show_info()

# Optional Parameters in Constructors
class Student:
    def __init__(self, name, age, grade="N/A"):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = Student("Arjun", 22)
student2 = Student("Abhishek", 23, "A")

student1.show_info()
student2.show_info()

class dog:
    def __init__(self,name,bread="husky"):
        self.name=name
        self.bread=bread

    def display(self):
        print(f"Name: {self.name}, breed: {self.bread}")

d=dog("Buddy")
d.display()
d2=dog("Max", "Labrador")
d2.display()


#example for static variable
class student:
    clg="gec" #class variable or static variable
    def __init__(self,name,course):
        self.name=name  #instance variable
        self.course=course #instance variable

    def show(self):
        print(f"Name: {self.name}, course: {self.course} and college is {self.clg}")

s=student("abc","ai")
s.show()

class con:
    def __init__(self,title):
        self.title=title

    def show(self):
        return self.title
c=con("python full stack")
res=c.show()
print(res)
print(c.show())

