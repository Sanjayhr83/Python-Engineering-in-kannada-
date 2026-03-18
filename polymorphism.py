# Polymorphism:Polymorphism means "many forms".The same function or method behaves differently in different situations.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

# Consider notifications in a social media app, where different types have the same send() method but behave uniquely:
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()

# Consider a fly() method in different classes:
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def call_fly(obj):
    obj.fly()

b = Bird()
a = Airplane()

call_fly(b)
call_fly(a)


# Consider an area() method in different classes:
class Shape:
    def area(self):
        print("Area")

class Circle(Shape):
    def area(self):
        print("Circle Area")

class Square(Shape):
    def area(self):
        print("Square Area")

c = Circle()
s = Square()
c.area()
s.area()

#Method Overriding:Method Overriding means redefining a method in the child class that is already defined in the parent class.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

obj = Child()
obj.show()

# Using super() in Overriding
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

obj = Child()
obj.show()

# Simple Combined Example (Very Important)
# Overloading style
def greet(name=None):
    if name:
        print("Hello", name)
    else:
        print("Hello Guest")

greet()
greet("Sanjay")

# Overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()

#method overloading is not support in python
