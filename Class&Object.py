import random


class Student:
    name = "Kusum Kumari"


s1 = Student()
print(s1.name)


class Car:
    color = "blue"
    brand = "mercedes"


car1 = Car()
print(car1.color)
print(car1.brand)


# Constructor
class Student:
    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome, ", self.name)

    def get_marks(self):
        return self.marks

    # Method that does not use the self parameter (work at class level)
    @staticmethod
    def college():
        print("NIT Durgapur")


s1 = Student("Kusum", 97)
print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())


# Practice question
# Create student class that takes name and marks of 3 students as arguments in constructor
# and then create a method to print the average

class Student1:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def Average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Average of three subject is ", avg)


s1 = Student1("Kajal Kumari", 97, 95, 92)
s1.Average()


# ---Practice Question--
# Create Account class with 2 attributes - balance and account no
# create methods for debit, credit and printing the balance

class Account:
    def __init__(self, account_no):
        self.balance = 0
        self.account_no = account_no

    def debit(self, amount):
        self.balance += amount

    def credit(self, amount):
        self.balance -= amount

    def Print_balance(self):
        print("Available balance is ", self.balance)


a1 = Account(1234567809)
a1.debit(1000)
a1.credit(200)
a1.Print_balance()

class Student2:
    def __init__(self):
        self.name = "Kusum"


s1 = Student2()
print(s1.name)
del s1.name
print(s1.name)