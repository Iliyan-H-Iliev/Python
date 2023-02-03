command = input()
first_num = int(input())
second_num = int(input())


def solve(operator, a, b):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


print(f"{solve(command, first_num, second_num)}")
