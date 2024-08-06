"""#For loop
for var in range(1,6):
    print(var)
print("next for")
for var in range(6):
    print(var)
print("next for")
for var in range(1,6,2):
    print(var)
print("---------------Print multiplication table---------------------")
n = int(input("Enter the no. :"))
for i in range(1,11):
    print(n," * ",i," = ",n * i)




#while loop
print("-------------------------------------------------------------------------------------------------------------")
n=10# initialization
while(n):#condition
    n=n-1
    print(n)#increment/decrement
n = int(input("Enter the no. :"))
i=1
while(i<=10):
    print(n," * ",i," = ",n*i)
    i+=1"""


#While true
"""while True:
    num1 = int(input("Enter 1st no: "))
    num2 = int(input("Enter 2nd no: "))
    print("Add :",num1+num2)
    repeat = input("Do you want to add again: \nwrite yes or no : ")
    if repeat == "No":
        break

#Nested loop
for i in range(1,4):
    for j   in range(1,11):
        print(j)
    print(i)

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = "")
    print()"""

for i in range(1,11):
    if i ==3:
        print("Add this song to fav")
    else:
        print(i)

print("Common multiple of 4 and 8 : ", end="")
for i in range(1,101):
    if (i % 4 == 0) and (i % 8 ==0):
        print(i,",", end="")