import math


def find_point(a, b):
    result = a ** 2 + b ** 2
    return math.sqrt(result)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

if find_point(x_1, y_1) <= find_point(x_2, y_2):
    print(f"({math.floor(x_1)}, {math.floor(y_1)})")
else:
    print(f"({math.floor(x_2)}, {math.floor(y_2)})")
