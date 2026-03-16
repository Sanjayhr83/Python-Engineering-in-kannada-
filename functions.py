#functions(def):A function is a block of code that performs a specific task and can be reused whenever needed.
# def function_name(parameters):
#     # Block of code


def greet():
    print("Hello, Good Morning!")
greet() #calling the function


#function with parameters
def greet(name):
    print("Hello, Good Morning!", name)
greet("srujan")

#function with input
def greet():
    name=input("Enter your name: ")
    print("Hello, Good Morning!", name)
greet()

#function with parameters
def marriage(boy,girl):
    print("The boy is {} and the girl is {}".format(boy,girl))
marriage("Ravi","kanniaka") #positional arguments

#function with default parameters
def marriage(boy,girl="priya"):
    print("The boy is {} and the girl is {}".format(boy,girl))
marriage(boy="Gowtham") #keyword arguments

#simple multiplication table
def cal():
    for i in range(1,11):
        print(f"3X{i}={3*i}")
cal()

#return statement
def add():
    a=14
    b=43
    return a+b
A=add()
print(A)

def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print("The sum is:", result)

#*args
print("*args")
def add_numbers(*args):
    return sum(args)
result = add_numbers(10, 20, 30)
print("The sum is:", result)

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result
print(total_sum(1, 2, 3, 4))

#**kwargs
print("*kwargs")
def add_numbers(**kwargs):
    return sum(kwargs.values())
result = add_numbers(a=10, b=20, c=30)
print("The sum is:", result)

def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
student_info(name="Anand", age=22, course="Python")

#lambda functions : A lambda function is a small anonymous function that can take any number of arguments but has only one expression.
print("lambda functions")
square = lambda x: x**2
print(square(5))

mul=lambda x,y:x*y
print(mul(5,6))
print(mul(8,7))
print(mul(7,5))

sum=lambda x: x**2
print(sum(8))

#Recursion: A function that calls itself is known as recursion.
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(9))
print(factorial(5))
print(factorial(0))

#nested functions:A nested function is a function defined inside another function.
def outer_function():
    def inner_function():
        print("Hello, I'm from inner function")
    inner_function()
outer_function()

def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()
outer_function("Anand")

