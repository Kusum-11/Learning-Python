# A built- in data type that stores set of values
# it can store element of different types(int, float, string, etc)

marks = [12,34,56,78]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["kusum", 7.17, 7.27,"NITDGP"]
print(student[0])
student[3] = "IIT"
print(student[3])

# list Slicing

print(student[:2])
print(student[-3:-1])
print(student[::-1])

# List Methods
list = [2,4,1,5,7,3]
list.append(9)
print(list)
list.sort()
print(list)
list = [2,4,1,5,7,3]
list.sort(reverse=True)
print(list)
list = [2,4,1,5,7,3]
list.reverse()
print(list)
list.remove(4)
print(list)
list.insert(3,100)
print(list)
list.pop(3)
print(list)

