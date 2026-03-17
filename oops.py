#oops(object-oriented programming system or structure)
#class:A class is a blueprint for creating objects. It defines the attributes and behaviors of the objects created from it.
#object:An object is an instance of a class. It is a real-world entity that has a state and behavior.

class Car:
    # Attributes
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    # Method
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of the class
my_car = Car("Toyota", "Corolla")
my_car.display_info()


#Attributes (Instance Variables) and Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects
person1 = Person("Arjun", 30)
person2 = Person("Megha", 25)

person1.greet()
person2.greet()

# Creating Multiple Objects from a Class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating multiple objects
dog1 = Dog("Rex", "Golden Retriever")
dog2 = Dog("Bolt", "Beagle")

dog1.bark()
dog2.bark()

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Sanjay")
print(s1.name)

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

c1 = Car("Toyota", 1000000)
c1.display()

#create mobile class and two attributes and object
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand :",self.brand)
        print("Price :",self.price)
#Creating objects
m=Mobile("Vivo",20999)
m.display()
m2=Mobile("Oppo",20000)
m2.display()

#create student class and two attributes and object
class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"{self.name} has scored {self.marks} marks")

# Creating objects
s=Student("Ravi",96)
s.display()