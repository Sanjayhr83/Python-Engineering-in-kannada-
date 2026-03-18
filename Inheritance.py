# Inheritance:Inheritance is a mechanism where one class acquires properties (attributes & methods) of another class.

"""class Parent:
    # parent code

class Child(Parent):
    # child code"""

class Family:
    def __init__(self, surname):
        self.surname = surname

class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name

child = Child("Gowda", "Ajay")
print(f"{child.name} {child.surname}")  # Inherits surname from Family


class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def display(self):
        print("This is child class")

c = Child()
c.show()     # inherited method
c.display()

#Types of Inheritance in Python
# Single Inheritance:One child inherits from one parent.
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

obj = B()
obj.show()
obj.display()

#Multiple Inheritance:One child inherits from multiple parents.
class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()
obj.display()


# Multilevel Inheritance:Inheritance chain where a class inherits from a parent class, which in turn inherits from another parent class.
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def print_data(self):
        print("Class C")

obj = C()
obj.show()
obj.display()
obj.print_data()

# Hierarchical Inheritance:Multiple children inherit from the same parent.
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(A):
    def print_data(self):
        print("Class C")

obj1 = B()
obj2 = C()
obj1.show()
obj1.display()
obj2.show()
obj2.print_data()

#Hybrid Inheritance:Combination of multiple inheritance types.
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()

#super() function
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  #super() calls the parent class constructor
        print("Child Constructor")

c = Child()

