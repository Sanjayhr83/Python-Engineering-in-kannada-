#local and global variables

#local variables : A local variable is a variable defined inside a function.
def local():
    a=10
    print(a)
local()

#modify local variable using nonlocal keyword
def cal():
    a=10
    a+=1
    print(a)
    def cal2():
        a=20
        a+=1
        print(a)
    cal2()
    def cal3():
        nonlocal a
        a=5
        print(a)
    cal3()
cal()

#global variables:A global variable is a variable defined outside the function.
def global_var():
    global a
    a=10
    print(a)
global_var()
print(a)

#modify global variable using global keyword
a=50
print(a)
def global_var():
    global a
    a+=10
    print(a)
global_var()
print(a)
