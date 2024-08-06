# print numbers from 1 to 100
count = 1
while count <= 100:
    print(count)
    count += 1

# Print numbers from 100 to 1
count = 100
while count >= 1:
    print(count)
    count -= 1

# print the multiplication table of a number n
number = int(input("Enter a number :"))
print("Table of ", number)
count = 1
while count <= 10:
    print(number, "*", count, " = ", number * count)
    count += 1

# Print thr element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]
count = 1
list = []
while count <= 10:
    sqr = count * count
    list.append(sqr)
    count += 1
print(list)

count = 0
while count < len(list):
    print(list[count])
    count += 1

# Search for a number x in this tuple using loop
val = tuple(list)
num = int(input("Enter a number for search :"))
count = 0
while count < len(val):
    if val[count] == num:
        print(val.index(num))
        break
    else:
        print("finding...")
    count += 1

# sum of n natural number
n = int(input("Enter the number to find sum of n natural no :"))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("sum", sum)

# WAP to find the factor of first n numbers(using for)
n = int(input("Enter a number to find the factor of first n numbers :"))
for i in range(1, n+1):
    print(f"factor of {i} is :", end="")
    for j in range(1, i+1):
        if i % j == 0:
            print(",", j, end="")
    print()

# WAP to find the factorial of first n numbers(using for)
n = int(input("Enter a number to find the factorial of first n numbers :"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)