def factorial(a):
    result = 1
    for i in range(a, 0, -1):
        result *= i
    return result


def divide_factorial(a, b):
    result = factorial(a) / factorial(b)
    return result


first_number = int(input())
second_number = int(input())

print(f"{divide_factorial(first_number, second_number):.2f}")
