# if the statement
a = 3
if a == 2:
    print("true")
print("False")

# if-else statement
Marks = 78
if Marks >= 45:
    print("Pass")
else:
    print("Fail")

#if-elif-else statement
Marks = 95
if Marks >= 60:
    print("1st Grade")
elif Marks >= 45:
    print("Pass")
else:
    print("Fail")

# Nested if statement
if Marks >= 45:
    print("Pass")
    if Marks >= 60:
        print("And 1st Grade")
        if Marks >= 90:
            print("And Excellent Performance")
else:
    print("Fail")

# Short Hand if Statement
# if condition: body of if
if Marks > 45: print("Pass")

# Short hand if else statement
# bodyOfIf if condition else bodyOfElse
print("Pass") if Marks >= 45 else print("Fail")

