numbers_list = input().split()

absolute_values = []


def abs_values(str_list):
    for el in str_list:
        absolute_values.append(abs(float(el)))

    return absolute_values


abs_values(numbers_list)
print(absolute_values)
