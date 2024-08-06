def sum(a, b):
    return a + b


sum = sum(5, 6)
print(sum)


def print_hello():
    print("hello")


for i in range(5):
    print_hello()


# WAF to print the length of a list(list is a parameter)
def len_of_list(list):
    return len(list)


list_length = len_of_list([1, 2, 3, 4, 5])
print(list_length)
list_length = len_of_list(["kus", "kaj", "app"])
print(list_length)


# WAF to find the factorial of n
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(factorial(10))
print(factorial(5))


# Recursion_____________________________
# function call itself repeatedly

def show(n):
    if n == 0:
        return 0
    print(n)
    show(n - 1)


show(5)


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


fact1 = fact(10)
print("fact of 10 is", fact1)


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


sum1 = sum(10)
print("sum of 10 is", sum1)


