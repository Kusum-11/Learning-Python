str = "Kusum"
print(str[0:3])
print(str[:3])
print(str[0:])
print(str[-3:-1])

Str = "i am kusum kumari studying in NIT Durgapur"
print(Str.endswith("pur"))
print(Str.capitalize())
print(Str) # does not change the existing variable
print(Str.replace("NIT","IIT"))
print(Str.find("kusum"))
print(Str.find("q")) # return -1 if does not exist in string
print(Str.count("i"))

#___________________________________________________________________________________
#Problem on string
#WAP to input users first name and print its length

name = input("Enter your name :")
x = name.find(" ")
first_name = name[:x]
print(len(first_name))

# WAP to find to find the occurance of "$" in the string
str = "$$$$$$$$$$$$"
print(str.count("$"))
