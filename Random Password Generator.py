import random
import string

password_len = int(input("Enter the length of password :"))
charValues = string.ascii_letters + string.digits + string.punctuation
# password = ""
# for i in range(password_len):
#     password += random.choice(charValues)


# Use List comprehension

password = "".join([random.choice(charValues) for i in range(password_len)])
print("Password :", password)