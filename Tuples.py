# it is a built-in data type
# tuple is immutable
tup = (1,2,4,5,2)
print(type(tup))
print(tup[3])
tup1 = (1)
print(type(tup1))
print(tup1)
tup1 = (1,)
print(type(tup1))
print(tup1)

# tuple slicing
print(tup[2:4])

# tuple Method
print(tup.index(4))
print(tup.count(10))

# ----------- Problems ------------------
#WAP to ask the user to enter names of their 3 favorite movies and store them in a list

# movies = []
# print("Enter the three movie name :")
# for i in range(0,3):
#     movie = input()
#     movies.append(movie)
# print(movies)

# Wap to check if a list contains a palindrome of elements.


# WAP to count the number of students with the "A" grade in the following tuple
tup = ("C", "D", "A", "A","B","B","A")
print("No of student with A Grade is : ",tup.count("A"))
lis = ["C", "D", "A", "A","B","B","A"]
lis.sort()
print("Shorted list :", lis)