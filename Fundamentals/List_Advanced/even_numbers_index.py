numbers_list = [int(x) for x in input().split(", ")]

even_list_index = [i for i in range(len(numbers_list)) if numbers_list[i] % 2 == 0]

print(even_list_index)
