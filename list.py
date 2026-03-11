#list(ordered, mutable(can be changed), allows duplicates, stores different type of data)

x=[1,2.4,"sanju",True,None]
print(x)
print(type(x))

list1 = [1, 2, 3]
list2 = ["apple", "banana", "mango"]
list3 = [10, "python", 3.5]

#accessing elements
list1 = [10,20,30,40]
print(list1[0]) #10
print(list1[2]) #30
print(list1[-1]) #40

#slicing
list1 = [10,20,30,40]
print(list1[1:3]) #20,30
print(list1[:2]) #10,20
print(list1[2:]) #30,40
print(list1[:]) #10,20,30,40

#list operations
list1 = [10,20,30,40]
list2 = [50,60,70,80]
print(list1 + list2) #10,20,30,40,50,60,70,80
print(list1 * 2) #10,20,30,40,10,20,30,40
print(10 in list1) #True
print(10 not in list1) #False
print(len(list1)) #4
print(max(list1)) #40
print(min(list1)) #10
print(sum(list1)) #100
print(list1.count(10)) #1
print(list1.index(10)) #0


a=[1,2,743,363,98,4,5,10]
print(a)
print(a.append(6))  #Add element at end
print(a)
print(a.insert(0,-9))   #Add element at index 0
print(a)
print(a.extend([7,8,9]))    #Add multiple elements at end
print(a)
print(a.remove(2))  #Remove specfic element
print(a)
print(a.pop(2))  #Remove by index
print(a)
print(a.reverse())  #Reverse the list
print(a)
print(sorted(a)) #Sort the list
print(a)
print(a.count(2))   #Count the element or occurrence
print(a.insert(0,-9))   #Insert element at position
print(a.clear())    #Clear the list
b=a.copy()  #Copy the list
print(b)

#nested list or matrix
z=[[1,2,3],
[4,5,6],
[7,8,9]]
print(z)     #print the matrix
print(z[0])  #print the first row
print(z[1])  #print the second row
print(z[2])  #print the third row
print(z[0][0]) #print the first element of first row
print(z[0][1]) #print the second element of first row
print(z[0][2]) #print the third element of first row
print(z[1][0]) #print the first element of second row
print(z[1][1]) #print the second element of second row
print(z[1][2]) #print the third element of second row
print(z[2][0]) #print the first element of third row
print(z[2][1]) #print the second element of third row
print(z[2][2]) #print the third element of third row

y=[[9,8,7],[6,5,4,],[4,3,2]]
print(y)
print(y[0])  #print the first row
print(y[1])  #print the second row
print(y[2])  #print the third row
print(y[0][0]) #print the first element of first row
print(y[0][1]) #print the second element of first row
print(y[0][2]) #print the third element of first row
print(y[1][0]) #print the first element of second row
print(y[1][1]) #print the second element of second row
print(y[1][2]) #print the third element of second row
print(y[2][0]) #print the first element of third row
print(y[2][1]) #print the second element of third row
print(y[2][2]) #print the third element of third row

