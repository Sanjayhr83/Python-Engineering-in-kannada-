#SOLID Principles in Python
# The SOLID principles are five guidelines that help us write clean, maintainable, and scalable object-oriented code. These are best practices followed by experienced developers to make code better.
# 🎯 S – Single Responsibility Principle 
# 🎯 O – Open/Closed Principle 
# 🎯 L – Liskov Substitution Principle 
# 🎯 I – Interface Segregation Principle 
# 🎯 D – Dependency Inversion Principle

# ✅ 1. Single Responsibility Principle (SRP)
# Definition: A class should have only one reason to change. That means, a class should do only one job.

# ❌ Bad Example:
class Student:
    def __init__(self, name):
        self.name = name

    def save_to_database(self):
        print("Saving to database...")

    def generate_report_card(self):
        print("Generating report card...")

# ✅ Good Example:
class Student:
    def __init__(self, name):
        self.name = name

class StudentDatabase:
    def save(self, student):
        print(f"Saving {student.name} to database...")

class ReportCard:
    def generate(self, student):
        print(f"Generating report card for {student.name}...")


# ✅ 2. Open/Closed Principle (OCP)
# Definition: Software entities (classes, functions, etc.) should be open for extension but closed for modification.

# ❌ Bad Example:
class Discount:
    def get_discount(self, customer_type):
        if customer_type == "regular":
            return 10
        elif customer_type == "premium":
            return 20

# ✅ Good Example:
class Discount:
    def get_discount(self):
        return 0

class RegularCustomer(Discount):
    def get_discount(self):
        return 10

class PremiumCustomer(Discount):
    def get_discount(self):
        return 20