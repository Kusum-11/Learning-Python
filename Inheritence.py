class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  # super keyword is used to access method of parent class
        self.name = name


car1 = ToyotaCar("fortuner","electric")
car2 = ToyotaCar("prius","Petrol")
print(car1.name)
print(car1.type)
car1.start()
car1.stop()
print(car2.name)
print(car2.type)
car2.start()
car2.stop()


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car3 = Fortuner("Diesel")
print(car3.type)
car3.start()


# Multiple Inheritance

class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)