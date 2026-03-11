#dictionaries(each key is unique, allow duplicate values,mutable,unordered)

my_dict={
    "key1": "value",
    "key2": "value"
}
print(my_dict)
print(type(my_dict))
print(len(my_dict))


date={#pentagon space
    "start":"24-1-2026",
    "end":"30-7-2026"
}
print(date)
print(type(date))
print(date["start"])
print(date["end"])


#aceessing element
student = {
    "name": "Sanjay",
    "age": 21
}
print(student["name"])
print(student["age"])

#acceess using get()
#get() method is safe way to access values because it donit raise error,value is not present in dictionary it return not found
student = {"name":"Sanjay", "age":21}
print(student.get("birth date","not fond")) 

#add new element
student = {"name":"Sanjay", "age":21}
student["city"] = "Bangalore"
print(student)

#updating
student = {"name":"Sanjay", "age":21}
student["age"]=23
print(student["age"])

#remove element
d = {"a":1, "b":2}
d.pop("a")  #remove element with key "a"
print(d)

d = {"a":1, "b":2}
d.popitem()
print(d)

d = {"a":1, "b":2}
del d["a"]
print(d)

d = {"a":1, "b":2}
d.clear()
print(d)

#dictionary methods
d = {"a":1, "b":2}
print(d.keys()) #print all keys
print(d.values()) #print all values
print(d.items()) #print all items
print(d.get("a")) #print value of key "a"
print(d.get("c", "not found")) #print value of key "c" or "not found" if key not present
print(d.update({"d":4})) #update dictionary
print(d.pop("a")) #remove element with key "a"
print(d.popitem()) #remove last element 
print(d.clear()) #remove all elements
print(d.setdefault("b",2)) #set default value
print(dict.fromkeys([1,2,3],0)) #create dictionary with keys and values

#simple shopping cart example
item1={
    "name":"chicken",
    "weight":1.5,
    "price": 250
}
item2={
    "name":"mutton",
    "weight":2,
    "price": 750
}
item=[item1,item2]
print(f"total price:{item1["price"]+item2["price"]}")   
print(f"total weight:{item1["weight"]+item2["weight"]}")