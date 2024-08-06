# Dictionary are used to store values in key:value pair
# it is unordered, mutable and don't allow duplicate key
info = {"key": "value",
        "name": "Kusum",
        "Roll no": "23CS4123",
        "subjects": ["Python", "C", "C++"],
        }
print(info)
print(type(info))
info["name"] = "Kusum Kumari"
print(info)

null_dict = {}  # initialize null dictionary

# nested dictionary
student = {
    "name": "Kusum Kumari",
    "subjects": {
        "phy": 97,
        "che": 98,
        "bio": 95

    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["phy"])

# dictionary function

print(student.keys())
print(list(student.keys()))

print(student.values())
print(list(student.values()))

print(list(student.items()))

print(student.get("name"))

student.update({"city": "Delhi"})
print(student)
