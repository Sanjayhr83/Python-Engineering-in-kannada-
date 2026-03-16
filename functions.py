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

