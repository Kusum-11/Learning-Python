a = "Hello, I'm Kusum Kumari"
print(a)
# to find the length of a
print(len(a))

#to find the no of times character is occoured
print(a.count("o"))

#to convert each letter into upper case
print(a.upper())

#to convert each letter into lower case
print(a.lower())

# to find the index of any char
print(a.index("o",1,20))

# to capitalize the first letter to capital
print(a.capitalize())

#to convert a string into lowerc ase
print(a.casefold())

#to find the index no of the character
print(a.find("k",12,19))

#to write variable inside a string
name = "John"
age = 24
b = "My name is ",name
print(b)
b = "My name is {}. and my age is {}"
print(b.format(name,age))

# to fill the given characters and centralize the string
print(name.center(20))
print(name.center(20,"*"))


a = "hello"
b= "hello123"
c = "122345"
d = "HELLO"
e = " "
f = "Hello 123@"
h = "Hello 123"
g = "1.234"
#isalnum- return if all char in string is alphanumeric
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(d,d.isalnum())
print(e,e.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())
print(h,h.isalnum())
print("-------------------------------------------------------")
#isalpha- return if all char in string is alphabet
print(a,a.isalpha())
print(b,b.isalpha())
print(c,c.isalpha())
print(d,d.isalpha())
print(e,e.isalpha())
print(f,f.isalpha())
print(g,g.isalpha())
print(h,h.isalpha())

print("--------------------isdecimal-----------------------------------")
#isdecimal- return if all char in string is decimal
print(a,a.isdecimal())
print(b,b.isdecimal())
print(c,c.isdecimal())
print(d,d.isdecimal())
print(e,e.isdecimal())
print(f,f.isdecimal())
print(g,g.isdecimal())
print(h,h.isdecimal())

print("--------------------isdigit-----------------------------------")
#isdigit- return if all char in string is digit
print(a,a.isdigit())
print(b,b.isdigit())
print(c,c.isdigit())
print(d,d.isdigit())
print(e,e.isdigit())
print(f,f.isdigit())
print(g,g.isdigit())
print(h,h.isdigit())

print("--------------------isnumeric-----------------------------------")
#isnumeric- return if all char in string is Numbers
print(a,a.isnumeric())
print(b,b.isnumeric())
print(c,c.isnumeric())
print(d,d.isnumeric())
print(e,e.isnumeric())
print(f,f.isnumeric())
print(g,g.isnumeric())
print(h,h.isnumeric())


print("--------------------islower-----------------------------------")
#islower- return if all char in string is lower case or not
print(a,a.islower())
print(b,b.islower())
print(c,c.islower())
print(d,d.islower())
print(e,e.islower())
print(f,f.islower())
print(g,g.islower())
print(h,h.islower())


print("--------------------isupper-----------------------------------")
#isupper- return if all char in string is upper case or not
print(a,a.isupper())
print(b,b.isupper())
print(c,c.isupper())
print(d,d.isupper())
print(e,e.isupper())
print(f,f.isupper())
print(g,g.isupper())
print(h,h.isupper())


print("--------------------isspace-----------------------------------")
#isspace- return if all char in string is white space
print(a,a.isspace())
print(b,b.isspace())
print(c,c.isspace())
print(d,d.isspace())
print(e,e.isspace())
print(f,f.isspace())
print(g,g.isspace())
print(h,h.isspace())


print("--------------------istitle-----------------------------------")
#istitle- return if all char in string follow the rules of title
print(a,a.istitle())
print(b,b.istitle())
print(c,c.istitle())
print(d,d.istitle())
print(e,e.istitle())
print(f,f.istitle())
print(g,g.istitle())
print(h,h.istitle())

print("--------------------endswith()-----------------------------------")
# endswith() - return true if the string ends with the required value
a = "Harry Potter"
print(a, a.endswith("r"))
print(a, a.endswith("t",6,9))

print("--------------------startswith()-----------------------------------")
# startswith() - return true if the string start with the required value
a = "Harry Potter"
print(a, a.startswith("H"))
print(a, a.startswith("P",6,9))

print("--------------------swapcase()-----------------------------------")
# swapcase() - lower case become upper nad vise versa
a = "Harry Potter"
print(a, a.swapcase())


print("--------------------strip()-----------------------------------")
# strip() - return true if the string start with the required value
a = "*****Harry Potter   "
print(a, a.strip())
print(a, a.strip("*, "))

# split() - split the string at the specified seperator and return the list
print("---------------------split()-------------------------------")
a = "#kusum#kumari#cute#TB"
print(a, a.split("#"))

#ljust() = Return the left justified version of the string
a = "Harry Potter"
x = a.ljust(20)
y = a.ljust(20, "@")
print(x, "is my favourite movie")
print(y, "is my favourite movie")

#rjust() = Return the right justified version of the string
a = "Harry Potter"
x = a.rjust(20)
y = a.rjust(20, "@")
print(x, "is my favourite movie")
print(y, "is my favourite movie")

#replace() - return a string where a specified value is replace by specified value
a = "My name is Kusum, Kusum plays Kabaddi"
print(a, a.replace("Kusum","Kajal"))

#rindex()/rfind() - Searches the string for a specified value and return the last position where it found
a = "Harry Potter and the prisoner of Azkaban Harry"
print(a, a.rindex("Harry",0,10))
print(a, a.rfind("Harry",6,50))

print("-------------------------------String Slicing-----------------------")
#String Slicing
a = "My name is Kusum, Kusum plays Kabaddi"
b = "0123456789"
print(a, a[0:10],"\n",a[15:25])
print(a[:6])
print(a[20:])
print(a[-10:])
print(b, b[4:7:2])
print(b,"reverse", b[::-1])