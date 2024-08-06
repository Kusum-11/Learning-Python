"""#WAP to find the sum of all even no upto 50
sum = 0
for i in range(1,51):
    if i%2 == 0:
        sum = sum +i
print("Sum :",sum)
#WAP to write 20 numbers and ther squared number
for i in range(1,21):
    print(i," :", i**2)
#WAP to find the sum of first 10 odd number using while loop
sum = 0
count = 0
for i in range(1,20):
    if i % 2 == 1:
        sum = sum + i
        count = count + 1
        if count == 10:
            break
print("Sum of 1st 10 odd no : ", sum)
#WAP to check is a no. is divisible by 8 and 12 upto 100 numbers
print("No divisible by 8 and 12 are : ", end="")
for i in range(1,101):
    if i % 8 ==0 and i % 12 == 0:
        print(",",i, end="")
print()


#WAP to create a biling sysytem at supermarket
while True:
    name = input("Enter Name : ")
    total = 0
    while True:
        quantity = int(input("Enter the quantity :"))
        amount = float(input("Enter the amount : "))
        total = total + (quantity * amount)
        repeat = input("Enter 'Y' for more entry 'N' for no entry ")
        if repeat == "N":
            break
    print("Total amount :", total)
    repeat_customer = input("Enter 'Y' for more customer 'N' for no entry ")
    if repeat_customer == "N":
        break
"""
#-----------------------------------------------------------------
A= "What is your name?"
b= len(A)
print("Length of the string is, ",b)
print("no. of times o is ocouring is ",A.count("o"))
print("lower string :",A.lower())
print("Upper string :",A.upper())
print("Convert into title :",A.title())
print("Find index of 'your' :",A.find("your"))

#-------------------PATTERN Printing----------------------
for i in range (1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

for i in range (1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()

for i in range (1,6):
    for j in range(1,i+1):
        print(i, end="")
    print()

for i in range (5, 0, -1):
    for j in range (1, i):
        print(i, end="")
    print()

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end="")
    print()
#----------------
for i in range(1,6):
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
#---------------------
for i in range (1,10):
    for j in range(1,i+1):
        print(i*j," ", end="")
    print()