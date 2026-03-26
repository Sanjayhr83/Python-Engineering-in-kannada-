# map(), filter(), and reduce()
"""
1. map() 
 Definition: Applies a given function to every element of an iterable. 
 Syntax: 
        map(function, iterable) 
 Returns a map object (iterator). Usually converted to a list or tuple.
"""

print("Map function: ")
# Example:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

div=list(map(lambda x: x/2, numbers))
print(div)  # Output: [0.5, 1.0, 1.5, 2.0, 2.5]


"""
2. filter() 
 Definition: Filters elements of an iterable based on a condition (returns only those for 
which the function returns True). 
 Syntax: 
        filter(function, iterable)
"""

print("Filter function: ")
# Example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

numbers = [10, 25, 30, 47, 50] 
result =list( filter(lambda x: x > 25, numbers) )
print(list(result))  # [30, 47, 50]


"""
3. reduce() 
 Definition: Applies a function cumulatively to the items of an iterable. 
 It’s like rolling computation (reduce the iterable into a single value). 
 Import needed: 
from functools import reduce 
 Syntax: 
        reduce(function, iterable[, initializer])
"""

print("Reduce function: ")
# Example:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120


from functools import reduce 
numbers = [1, 2, 3, 4, 5] 
def add(x, y): 
    return x + y 
result = reduce(add, numbers) 
print(result)  # 15


from functools import reduce 
numbers = [10, 20, 5, 8, 100, 3] 
result = reduce(lambda a, b: a if a > b else b, numbers) 
print(result)  # 100


#Practical Example: Processing Student Scores 
from functools import reduce 
scores = [45, 67, 89, 34, 76, 90] 
# 1. Increase all scores by 5 using map 
updated = list(map(lambda x: x + 5, scores)) 
# 2. Filter only passing students (>= 50) 
passed = list(filter(lambda x: x >= 50, updated)) 
# 3. Find the total marks of all passed students using reduce 
total = reduce(lambda x, y: x + y, passed) 
print("Updated Scores:", updated) 
print("Passed Students:", passed) 
print("Total Marks:", total) 