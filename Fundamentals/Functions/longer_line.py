import math


def line(x1, y1, x2, y2):
    result = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return math.sqrt(result)


def point(x1, y1):
    result = x1 ** 2 + y1 ** 2
    return math.sqrt(result)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

line_1 = line(x_1, y_1, x_2, y_2)
line_2 = line(x_3, y_3, x_4, y_4)

x1y1 = point(x_1, y_1)
x2y2 = point(x_2, y_2)
x3y3 = point(x_3, y_3)
x4y4 = point(x_4, y_4)


if line_1 >= line_2:
    if x1y1 <= x2y2:
        print(f"({math.floor(x_1)}, {math.floor(y_1)})({math.floor(x_2)}, {math.floor(y_2)})")
    else:
        print(f"({math.floor(x_2)}, {math.floor(y_2)})({math.floor(x_1)}, {math.floor(y_1)})")
else:
    if x3y3 <= x4y4:
        print(f"({math.floor(x_3)}, {math.floor(y_3)})({math.floor(x_4)}, {math.floor(y_4)})")
    else:
        print(f"({math.floor(x_4)}, {math.floor(y_4)})({math.floor(x_3)}, {math.floor(y_3)})")
