# WAP to display a persons name, age and address in three different line
print("my name is kusum\nage 23\naddress is dehri on sone ")

name =input("enter name : ")
age = int(input("Enter the age :"))
phone_no = input("Enter phone_no :")
address = input("Enter address :")
print(name)
print(age)
print(address)

# WAP to swap two numbers

a = int(input("enter first number: "))
b = int(input("enter second number: "))
temp = a
a = b
b = temp
print(" After swap first number a :", a)
print(" After swap second number b :", b)

# method 2
a = int(input("enter first number: "))
b = int(input("enter second number: "))
a, b = b, a
print(" After swap first number a :", a)
print(" After swap second number b :", b)

# WAP to convert float into integer

x = 12.4
print(x, type(x))
x = int(x)
print(x, type(x))
a = int(input("Enter a no. :"))
print(a, type(a))
a = float(a)
print("after conversion :",a, type(a))
