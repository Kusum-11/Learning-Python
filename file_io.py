# # Read mode
# f = open("demo.txt", "r")
# # data = f.read()
# # data = f.read(10)
# data = f.readline()
# print(data)
# print(type(data))
# f.close()
#
# # Write mode
# f = open("demo.txt", "w")
# f.write("I also want to learn C, C++.")
# f.close()
#
# f = open("demo.txt", "a")
# f.write("\nThen I move to learn AI/ML and OOPS concept")
# f.close()
#
# with open("demo.txt", "r") as f:
#     f.read()
#     print(data)
#
# with open("demo.txt", "w") as f:
#     f.write("New data")

# Deleting a file
# import os
# os.remove("demo.txt")

# -----------------------------------------------
with open("practice.txt", "w") as f:
    f.write("Hi everyone \nwe are learning python")
with open("practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Found")
    else:
        print("Not Found")

new_data = data.replace("python", "java")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


def check_for_word():
    with open("practice.txt", "r") as f:
        data = True
        line = 1
        while data:
            data = f.readline()
            if data.find("learning") != -1:
                print("Found",line)
                return
            line += 1
    return -1

print(check_for_word())

with open("practice.txt", "w") as f:
    f.write("1,2,76,84,90,101")

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

data = data.split(",")
count = 0
for val in data:
    if(int(val) % 2 == 0):
        count += 1
# len = len(data)
print(count)