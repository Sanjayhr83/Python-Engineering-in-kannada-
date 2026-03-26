# Abstraction:Abstraction means hiding internal implementation details and showing only essential features to the user.

class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts with key")

class Bike(Vehicle):

    def start(self):
        print("Bike starts with kick")

c = Car()
c.start()
b = Bike()
b.start()

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def area(self):
        print("Area of square")

s = Square()
s.area()