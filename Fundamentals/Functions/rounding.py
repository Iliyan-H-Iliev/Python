def rounding(a):
    rounded_list = []
    for el in a:
        rounded_list.append(round(el))
    return rounded_list


numbers_input = [float(x) for x in input().split()]

print(rounding(numbers_input))
