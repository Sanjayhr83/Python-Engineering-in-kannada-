a=12    #int
b=12.4    #float(decimal number)
c="sanju"    #string
d=True    #boolean
e=None    #None
f=1+2j    #complex
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))

#type casting
#String to Integer
a = "10"
b = int(a)

print(b)
print(type(b))

#Integer to Float
a = 5
b = float(a)

print(b)
print(type(b))

#Integer to String
a = 100
b = str(a)

print(b)
print(type(b))


#Swaping two variables
a=20
b=30
print(a)
print(b)
a,b=b,a #method 1 to swap variables
print(a)
print(b)

c=98
d=76
print(c)
print(d)
temp=c  #using temp variable to swap variables
c=d
d=temp
print(c)
print(d)