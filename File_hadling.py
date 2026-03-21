"""
File Handling in Python :
File handling allows us to read from and write to files — a common task in almost every real-world application (storing data, logs, reports, etc.).

📁 Why File Handling?
To save user data permanently (like notes, records, etc.)

To read content from a file (like student marks, exam results)

Helps build real applications like:

Address books
Billing systems
Exam report generators
📌 Python File Modes
Mode	    Meaning         	                Use Case
'r'	    Read (default mode)	                Read an existing file
'w' 	Write (overwrites if file exists)	Write new content
'a'	    Append (adds content at the end)	Add data without deleting old
'x'	    Create (fails if file exists)	    Create new file safely
'b'	    Binary mode	                        For images, videos, etc.
't'	    Text mode (default)	                For text files
"""

"""
 Common Errors
Error	                        Cause
FileNotFoundError           Trying to read a missing file
PermissionError	            Access denied
IsADirectoryError	        Trying to open a folder as file
"""

file=open("notes.txt","w")  # Opening a File in write mode
file.write("Hello, World!")
file.write("\nI am learning File Handing in python")
file.close()

file=open("notes.txt","r")  # Opening a File in read mode
print(file.read())
contents=file.read()
print(contents)
file.close()


# Reading From a File
# 1. read() – Reads entire file
file = open("notes.txt", "r")
print(file.read())
file.close()

# 2. readline() – Reads one line at a time
file = open("notes.txt", "r")
print(file.readline())
file.close()

# 3. readlines() – Reads all lines into a list
file = open("notes.txt", "r")
print(file.readlines())
file.close()

# Writing to a File
# write() – Overwrites entire file
file = open("data.txt", "w")
file.write("Namaskara Bengaluru!\n")
file.write("Python is awesome!")
file.close()

# Appending to a File
file = open("data.txt", "a")
file.write("\nThis line is added later.")
file.close()

# Using with Statement (Best Practice)
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

#Writing List of Data to File
students = ["Ravi","Rahul","Shashank","Loki","Abhi","Ram", "Meena", "Dinesh"]
with open("notes.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

#  Reading File and Processing Each Line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())