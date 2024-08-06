class Person:
    __name = "Kusum"  # here __ denotes that attribute name is private

    def __hello(self):  # here __ denotes functon hello is private
        print("hello person !")

    def welcome(self):
        self.__hello()


p1 = Person()
p1.welcome()
