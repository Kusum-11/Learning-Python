# two types of typecasting
# implicit and explicit typecasting

# implicit typecasting
name = "kusum"
age = 23
print(type(name))
print(type(age))


a = 123
b = 12.2
print(type(a))
print(type(b))
c = a+b
print(type(c))
print(c)

#explicit typecasting
a = int(a)
c = int(c)
print("After Explicit typecasting, c :", c,type(c))
