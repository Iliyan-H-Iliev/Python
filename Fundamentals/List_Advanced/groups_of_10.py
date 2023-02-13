from math import ceil

numbers_list = [int(x) for x in input().split(", ")]

groups = ceil(max(numbers_list) / 10)

min_boundary = 1
max_boundary = 10

for _ in range(groups):
    list_of_numbers = []

    for el in numbers_list:
        if min_boundary <= el <= max_boundary:
            list_of_numbers.append(el)

    print(f"Group of {max_boundary}'s: {list_of_numbers}")

    min_boundary += 10
    max_boundary += 10
