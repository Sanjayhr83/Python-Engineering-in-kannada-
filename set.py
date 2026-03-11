#set{unordered,unindexed, not allow duplicates values,mutable, sotres diff types}
#it is perform union(|),intersection(&),difference(-)
s = {10, 20, 30, 40}
print(s)
print(type(s))
print(len(s))

s1 = {1, 2, 3}
s2 = {"apple", "banana", "mango"}
s3 = {10, "python", 3.5}

#empty set
s = set()
print(s)
print(type(s))

#do not allow duplicates
s = {10, 20, 30, 30, 40, 10, 20}
print(s)


#union
a = {1,2,3}
b = {3,4,5}
print("Union:",a | b) 

#intersection
print("Intersection:",a & b)

#difference
print("Difference:",a - b)

#symmetric difference
print("Symmetric difference:",a ^ b)

#membership test
a = {1,2,3,7,8}
print(1 in a)
print(4 in a)
print(1 not in a)
print(4 not in a)


#methos in sets
s = {1,2,3}
s.add(4)    #add element
print(s)

s = {1,2}
s.update([3,4]) #add multiple elements
print(s)

s = {1,2,3}
s.remove(2) #remove specific element
print(s)

s = {1,2,3}
s.discard(2) #Removes element without error if not found.
print(s)

s = {10,20,30}
s.pop() #it is remove random element.
print(s)

s = {1,2,3}
s.clear() #Removes all elements
print(s)

s = {1,2,3}
s2 = s.copy() #Creates a shallow copy
print(s2)