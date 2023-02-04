def multiplication(a, b, c):
    result = ""
    if a == 0 or b == 0 or c == 0:
        result = "zero"
    elif (a < 0 < b and c > 0) or (b < 0 < a and c > 0) \
            or (c < 0 < a and b > 0) or (a < 0 and b < 0 and c < 0):
        result = "negative"
    else:
        result = "positive"
    return result


numb_1 = int(input())
numb_2 = int(input())
numb_3 = int(input())

print(multiplication(numb_1, numb_2, numb_3))
