def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    result = subtract(add(a, b), c)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
