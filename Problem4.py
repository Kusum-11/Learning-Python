#WAP to write a Fibonaci series upto 10 numbers.
a = 0
b = 1
print(a,",", b, end="")
for i in range(8):
    c = a+b
    a = b
    b = c
    print(",",c, end="")
print()
# WAP to check if a number is prime or not.
n = int(input("Enter a no to check if no. is prime or not"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Number is Prime Number")
else:
    print("Number is not a Prime Number")
# WAP to find a palindrome of integers.
n = input("Enter the integer numer for palindrom  :")
n = n[::-1]
print("Palindrom of the given no is : ", n)
#WAP to create an area calculator
n = int(input("Press: \n1 to find the Area of Rectange\n2 to find Area of Square\n3 to find area of triangle "))
if n == 1:
    length = int(input("Enter length: "))
    width = int(input("Enter Width: "))
    area = length * width
    print("Area :", area)
elif n== 2:
    side = int(input("Enter length of any side: "))
    area = side * side
    print("Area :", area)
elif n == 3:
    length = int(input("Enter length: "))
    height = int(input("Enter height: "))
    area = 0.5 * length * height
    print("Area :", area)
else:
    print("Enter the correct input")