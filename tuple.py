#tuple(ordered, immutable(cannot be changed), allows duplicates, stores different type of data)
#it is faster than list
t=(1,2.4,"sanju",True,None)
print(t)
print(type(t))
print(len(t))

#empty tuple
t=()
print(t)
print(type(t))

t=(18,) #A comma is required for single element tuple
print(t)

#Accessing Tuple Elements
t = (10, 20, 30, 40)
print(t[0])
print(t[2])

#. Tuple Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])   # (20, 30, 40)
print(t[0::2])  # (10, 30, 50)
print(t[0:4:-1]) # () - empty because start > end with negative step
print(t[::-1])  # (50, 40, 30, 20, 10)

#Concatenation
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)

#Repetition
t = (1,2)
print(t * 3)


#Membership Operators
t = (10,20,30)
print(20 in t)
print(50 not in t)


#Iteration
t = (10,20,30)
for i in t:
    print(i)


#count()
t = (10,20,10,30)
print(t.count(10))

#index()
t = (10,20,10,30)
print(t.index(10))

#packing
t=10,20,30
print(t)
print(type(t))

#unpacking
t = (10,20,10,30)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)

#converting
#Tuple → List
t = (1,2,3)
l = list(t)
print(l)
print(type(l))


#List → Tuple
l = [1,2,3]
t = tuple(l)
print(t)
print(type(t))