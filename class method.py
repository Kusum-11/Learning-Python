class Person:
    name = "anonymous"
    name1 = "anonymous"

    # def changeName(self, name):
    #     self.name = name  # does not change the class variable instead of creating one new variable in object
    #     self.__class__.name1 = name  # direct change in class variable

    @classmethod  # used to bound the class and receives the class as an first argument
    def changeName(cls, name):
        cls.name = name
        cls.name1 = name

p1 = Person()
p1.changeName("Kusum Kumari")
print(p1.name,p1.name1)
print(Person.name,Person.name1)


class Student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        # self.percentage = str((self.phy+self.che+self.math)/3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy+self.che+self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"



s1 = Student(98,97,96)
print(s1.percentage)

s1.phy =86
print(s1.phy)
print(s1.percentage)

# s1.calcPercentage()
# print(s1.percentage)