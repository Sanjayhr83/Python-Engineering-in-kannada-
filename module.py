"""
module:A module is simply a .py file containing functions, classes, or variables.
 We can import it and use its code in another file.
 """
import math
print(math.sqrt(25))  # Output: 5.0


"""
Package:
A package is a folder containing multiple modules and an optional __init__.py file.
Helps organize large projects into folders.
school/
├── __init__.py
├── students.py
├── teachers.py
"""

from school import students
students.add_student("Meghana")

"""
 Python Libraries:
 A library is a collection of modules and packages made for a specific purpose.
Popular Libraries in Python:
Library	            Purpose
math	        Math functions
random	        Random number generation
datetime	    Date and time
os	            Operating system tasks
sys	            System-specific parameters
json	        Work with JSON data
re	            Regular expressions

"""

import random
print(random.randint(1, 10))  # Random number between 1 and 10

# pip install wikipedia
import wikipedia
print(wikipedia.summary("Virat Kohli"))
