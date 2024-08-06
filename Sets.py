# Set is a collection of unordered items
# Set is mutable but
# Each element in the set must be unique and immutable
# can not store list and dictionary because they are mutable

collection = {1, 2, 3, 4, "Hello", 4, 5}
print(collection)
print(type(collection))

# initialization of empty set
collection1 = set()

# Function in Set
collection1.add(1)
collection1.add(2)
collection1.add("Kusum")
collection1.add((1, 2, 3))
collection1.remove(2)
print(collection1)

collection1.clear()
print(len(collection1))

collection1.add(1)
collection1.add(2)
collection1.add("Kusum")
collection1.add((1, 2, 3))
print(collection1)

# print("1st pop",collection1.pop())
# print("2nd pop",collection1.pop())
# print("3rd pop",collection1.pop())

print("Collection :", collection)
print("collection1", collection1)
print(collection.intersection(collection1))
print(collection1.union(collection))

# Practice question on set and dictionary
# Store following meaning in a python dictionary
dict = {
    "table": ["a piece of furniture", "list of fats and figures"],
    "cat": "a small animal"
}
print(dict)

# You are given a list of subjects for student. assume one classroom is required for one subject . how many classroom
# is needed

list = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
list = set(list)
print(list)
print(len(list))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary starts with empty dictionary and
# add one by one . Use name as key and marks as value.

# print("Enter the marks of 3 subject :")
# marks = {}
# for i in range(3):
#     sub = input("Subjects :")
#     mark = float(input("Marks :"))
#     marks.update({sub: mark})
#
# print(marks)

# figure out a way to store 9 & 9.0 as a separate values in a set
set0 = {9, "9.0"}
value = {("float",9.0),("int",9)}
print(set0)
print(value)
print(type(value))