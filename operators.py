#Arithmetic Operators(+,-,*,/,%,**,//)
print("Arithmetic Operators")
a=50
b=20
print(a+b)  #70
print(a-b)  #30
print(a/b)  #2.5
print(a*b)  #1000
print(a%b)  #10
print(a**b) #50^20(9536374230000000)
print(a//b) #2


#Comparison (Relational) Operators
print("Comparison (Relational) Operators")
a = 10
b = 5

print(a == b)   #False
print(a != b)   #True
print(a > b)    #True
print(a < b)    #False
print(a >= b)   #True
print(a <= b)   #False

#Assignment Operators
print("Assignment Operators")
a=5
print(a)    #5
a+=3
print(a)    #8
a-=3
print(a)    #5
a*=3
print(a)    #15
a/=3
print(a)    #5.0
a%=3
print(a)    #2.0
a**=3
print(a)    #8.0
a//=3
print(a)    #2.0

#Logical Operators(and, or, not)
print("Logical Operators")
a=5
b=10
print(a and b)  #10
print(a or b)   #5
print(not a)    #False
print(a > 5 and b < 10) #False
print(a > 5 or b > 10) #False
print(not(a > 5)) #True

#Bitwise Operators(&, |, ^, ~, <<, >>)
print("Bitwise Operators")
a=5
b=10
print(a & b)    #0 (AND)
print(a | b)    #15 (OR)
print(a ^ b)    #15 (XOR)
print(~a)       #-6 (NOT)
print(a << 2)   #20 (LEFT SHIFT)
print(a >> 2)   #1 (RIGHT SHIFT)

#Membership Operators(in, not in)
print("Membership Operators")
a=[1,2,3,4,5]
print(1 in a)   #True
print(6 not in a)   #True
list1 = [1,2,3,4]
print(2 in list1)   #True
print(5 in list1)   #False
print(5 not in list1)   #True

#Identity Operators(is, is not)
print("Identity Operators")
a=5
b=5
print(a is b)   #True
print(a is not b)   #False
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)   #True
print(a is c)   #False
print(a is not c)   #True

