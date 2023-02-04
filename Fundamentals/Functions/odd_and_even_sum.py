def odd_sum(n):
    result = sum([el for el in n if el % 2 == 1])
    return result


def even_sum(n):
    result = sum([el for el in n if el % 2 == 0])
    return result


numbers_as_string = input()
numbers_as_digits = []
for i in range(0, len(numbers_as_string)):
    numbers_as_digits.append(int(numbers_as_string[i]))


print(f"Odd sum = {odd_sum(numbers_as_digits)}, Even sum = {even_sum(numbers_as_digits)}")
