# 1. Banking System Simulation
# Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.
# Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
# Emphasize encapsulation, inheritance and polymorphism.

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   # Encapsulation (private)
    # Deposit
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New Balance: {self.__balance}")
    # Withdraw (base behavior)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Balance: {self.__balance}")
        else:
            print("Insufficient balance")
    # Getter
    def get_balance(self):
        return self.__balance

# 🔹 Savings Account (Inheritance + Polymorphism)
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=5):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest added: {interest}")

# 🔹 Current Account (Overdraft Feature)
class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=500):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit
    # Method Overriding (Polymorphism)
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            # Accessing private via deposit logic workaround
            super().deposit(-amount)
            print(f"{amount} withdrawn with overdraft. Balance: {new_balance}")
        else:
            print("Overdraft limit exceeded")

# Savings Account
s = SavingsAccount("Sanjay", 1000)
s.deposit(500)
s.withdraw(300)
s.add_interest()
print("Final Balance:", s.get_balance())

# Current Account
c = CurrentAccount("Ravi", 1000)
c.withdraw(1200)   # uses overdraft
c.withdraw(2000)   # exceeds limit
print("Final Balance:", c.get_balance())

# 2. Library Management System
# Create a library system that keeps track of books, borrowers, and availability. Allow borrowing, returning, and viewing available books.
# Include due dates, penalties for late returns, and unique IDs for books and users.
# Focus on class relationships and method responsibilities.

from datetime import datetime, timedelta
# 🔹 Book Class
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_available = True

# 🔹 User Class
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = {}

# 🔹 Library Class
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
    # Add Book
    def add_book(self, book):
        self.books[book.book_id] = book
    # Add User
    def add_user(self, user):
        self.users[user.user_id] = user
    # Borrow Book
    def borrow_book(self, user_id, book_id):
        user = self.users[user_id]
        book = self.books[book_id]
        if book.is_available:
            due_date = datetime.now() + timedelta(days=7)
            user.borrowed_books[book_id] = due_date
            book.is_available = False
            print(f"{user.name} borrowed '{book.title}'")
            print("Due Date:", due_date.date())
        else:
            print("Book not available")
    # Return Book
    def return_book(self, user_id, book_id):
        user = self.users[user_id]
        book = self.books[book_id]
        if book_id in user.borrowed_books:
            due_date = user.borrowed_books.pop(book_id)
            book.is_available = True
            # Check late return
            today = datetime.now()
            if today > due_date:
                late_days = (today - due_date).days
                penalty = late_days * 10
                print(f"Late return! Penalty: ₹{penalty}")
            else:
                print("Returned on time")

            print(f"{book.title} returned successfully")
        else:
            print("This book was not borrowed")
    # View Available Books
    def show_books(self):
        for book in self.books.values():
            if book.is_available:
                print(book.book_id, "-", book.title)

lib = Library()
# Add Books
lib.add_book(Book(1, "Python Basics"))
lib.add_book(Book(2, "Data Structures"))
# Add User
lib.add_user(User(101, "Sanjay"))
# Borrow Book
lib.borrow_book(101, 1)
# Show Available Books
lib.show_books()
# Return Book
lib.return_book(101, 1)


# 3. Hospital Patient Management
# Create a hospital management system that tracks doctors, patients, and appointments.
# Doctors can have specialties, and patients may have different ailments.
# Each appointment should store the doctor-patient relationship, along with the date and time.
# Add functionality for doctors' schedules and ensuring no double booking.

from datetime import datetime

# 🔹 Doctor Class
class Doctor:
    def __init__(self, doc_id, name, specialty):
        self.doc_id = doc_id
        self.name = name
        self.specialty = specialty
        self.schedule = []   # list of appointment times


# 🔹 Patient Class
class Patient:
    def __init__(self, patient_id, name, ailment):
        self.patient_id = patient_id
        self.name = name
        self.ailment = ailment


# 🔹 Appointment Class
class Appointment:
    def __init__(self, doctor, patient, date_time):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time


# 🔹 Hospital Class
class Hospital:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.appointments = []

    # Add Doctor
    def add_doctor(self, doctor):
        self.doctors[doctor.doc_id] = doctor

    # Add Patient
    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    # Book Appointment
    def book_appointment(self, doc_id, patient_id, date_time):
        doctor = self.doctors[doc_id]
        patient = self.patients[patient_id]

        # Check double booking
        if date_time in doctor.schedule:
            print("Doctor not available at this time")
            return

        # Create appointment
        appointment = Appointment(doctor, patient, date_time)
        self.appointments.append(appointment)

        # Update doctor schedule
        doctor.schedule.append(date_time)

        print(f"Appointment booked: {doctor.name} with {patient.name} at {date_time}")

    # Show Appointments
    def show_appointments(self):
        for a in self.appointments:
            print(a.doctor.name, "-", a.patient.name, "-", a.date_time)

h = Hospital()

# Add Doctors
h.add_doctor(Doctor(1, "Dr. Smith", "Cardiology"))
h.add_doctor(Doctor(2, "Dr. John", "Dermatology"))

# Add Patients
h.add_patient(Patient(101, "Sanjay", "Heart Problem"))
h.add_patient(Patient(102, "Ravi", "Skin Allergy"))

# Book Appointments
time1 = datetime(2026, 3, 20, 10, 0)

h.book_appointment(1, 101, time1)
h.book_appointment(1, 102, time1)  # double booking

# Show Appointments
h.show_appointments()

# 4. E-Commerce Platform Prototype
# Simulate a basic e-commerce platform where customers can browse products, add them to a cart, and place orders.
# Use OOP principles to manage inventory, pricing (e.g., discounts), and order tracking.
# Integrate functionality for calculating taxes and shipping costs dynamically.

# 🔹 Product Class
class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percent):
        return self.price - (self.price * percent / 100)


# 🔹 Customer Class
class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.cart = Cart()


# 🔹 Cart Class
class Cart:
    def __init__(self):
        self.items = {}   # {product: quantity}

    def add_item(self, product, qty):
        if product.stock >= qty:
            self.items[product] = self.items.get(product, 0) + qty
            product.stock -= qty
            print(f"{product.name} added to cart")
        else:
            print("Not enough stock")

    def get_total(self):
        total = 0
        for product, qty in self.items.items():
            total += product.price * qty
        return total


# 🔹 Order Class
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.status = "Placed"

    def calculate_total(self):
        subtotal = sum(p.price * q for p, q in self.items.items())

        tax = subtotal * 0.10        # 10% tax
        shipping = 50 if subtotal < 500 else 0

        total = subtotal + tax + shipping

        print("Subtotal:", subtotal)
        print("Tax:", tax)
        print("Shipping:", shipping)
        print("Total:", total)

        return total


# 🔹 Store Class
class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.pid] = product

    def show_products(self):
        for p in self.products.values():
            print(p.pid, p.name, p.price, "Stock:", p.stock)

store = Store()
# Add products
p1 = Product(1, "Laptop", 50000, 10)
p2 = Product(2, "Phone", 20000, 5)
store.add_product(p1)
store.add_product(p2)
store.show_products()
# Customer
c = Customer(101, "Sanjay")
# Add to cart
c.cart.add_item(p1, 1)
c.cart.add_item(p2, 2)
# Place order
order = Order(c, c.cart.items)
order.calculate_total()

# 5. Student Report Card Generator
# Build a system that collects student data and subject-wise marks to generate a report card.
# Include grade calculation, average score, and pass/fail result.
# Use encapsulation for mark storage and method abstraction for result generation.

# 🔹 Student Class
class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.__marks = {}   # Encapsulation (private)

    # Add marks
    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    # Get marks
    def get_marks(self):
        return self.__marks

    # Calculate total
    def get_total(self):
        return sum(self.__marks.values())

    # Calculate average
    def get_average(self):
        return self.get_total() / len(self.__marks)

    # Calculate grade
    def get_grade(self):
        avg = self.get_average()

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    # Pass/Fail
    def get_result(self):
        for m in self.__marks.values():
            if m < 35:
                return "Fail"
        return "Pass"

    # Display Report Card
    def display_report(self):
        print("\n--- Report Card ---")
        print("ID:", self.sid)
        print("Name:", self.name)

        for sub, marks in self.__marks.items():
            print(sub, ":", marks)

        print("Total:", self.get_total())
        print("Average:", self.get_average())
        print("Grade:", self.get_grade())
        print("Result:", self.get_result())
s = Student(101, "Abhiram")
s.add_marks("Math", 85)
s.add_marks("Science", 90)
s.add_marks("English", 70)
s.add_marks("CS", 95)
s.display_report()