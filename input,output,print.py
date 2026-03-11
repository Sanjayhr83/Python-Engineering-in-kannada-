#input, output and print
a=int(input("enter a number: "))
b=float(input("enter a number: "))
print("a is",a)
print("b is",b)
print("sum is",a+b)

#take user input like name,age and concate the string
boy=input("enter boy name: ")
boy_age=int(input("enter boy age: "))
girl=input("enter girl name: ")
girl_age=int(input("enter girl age: "))
age= boy_age - girl_age
print(boy + " loves " + girl, "and their age difference is", abs(age))  #abs means absolute

x=input("enter you name: ")
y=int(input("enter your age: "))
print("Hello, {}! you are {} years old".format(x,y))