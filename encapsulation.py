#Encapsulation:Encapsulation means wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to data.
# | Type      | Syntax | Meaning                      |
# | --------- | ------ | ---------------------------- |
# | Public    | `x`    | Accessible everywhere        |
# | Protected | `_x`   | Internal use (by convention) |
# | Private   | `__x`  | Restricted access            |


class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)

#simple example
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

b = Bank(1000)
b.deposit(500)
b.show_balance()

# Encapsulation Example (Public, Protected, Private)
class Student:
    def __init__(self, name, age, marks):
        self.name = name        # Public
        self._age = age         # Protected
        self.__marks = marks    # Private

    # Getter for private variable
    def get_marks(self):
        return self.__marks

    # Setter for private variable
    def set_marks(self, marks):
        self.__marks = marks

# Creating object
s = Student("Sanjay", 21, 85)

# Accessing Public Variable
print("Public:", s.name)

# Accessing Protected Variable
print("Protected:", s._age)

# Accessing Private Variable (Not directly allowed)
# print(s.__marks)   ❌ Error

# Access using getter
print("Private (using getter):", s.get_marks())

# Modify using setter
s.set_marks(95)
print("Updated Marks:", s.get_marks())

class bank:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.__balance = balance

    def getter(self):
        if self.__balance >0:
            self.__balance = self.__balance
        return self.__balance,self.acc_no

b=bank(1234,1000)
res=b.getter()
print(res)