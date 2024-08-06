# WAP to check a no is Positive or not

a = input(print("Enter a no :"))
a = int(a)
print("Positive ") if a>=0 else print("Negative")
#WAP to check weather a no is odd or even
a = input(print("Enter a no :"))
a = int(a)
print("even") if a%2 == 0 else print("Odd")
#WAP to create calculator
a = input(print("Enter a 1st no :"))
a = int(a)
b = input(print("Enter a 2nd no :"))
b = int(b)
add= a+b
sub = a-b
mult = a*b
div = a/b
print("Enter 1 for addition \n 2 for Substraction\n3 for Multipilication\n4 for division ")
result = int(input())
if result ==1:
    print("Addition = ",add)
elif result ==2:
    print("Substraction = ",sub)
elif result ==3:
    print("Multiplication = ",mult)
elif result ==4:
    print("Division = ",div)
else:
    print("Enter correct no.")


#WAP to check wether passed leter is a vowel or not

letter = input("Enter the letter :")
if letter in "aeiouAEIOU":
    print("it is a vowel")

#WAP to check if a no is a single digit no, 2 digit no. .. upto 5 digit
a = int(input(print("Enter a no :")))
if a<10:
    print("Single digit no.")
elif a<100:
    print("Double digit no.")
elif a<1000:
    print("Triple digit no.")
elif a<10000:
    print("Four digit no.")
elif a<100000:
    print("Five digit no.")
else:
    print("Greater then 5 digit no")


