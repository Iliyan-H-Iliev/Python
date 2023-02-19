list_input = [int(x) for x in input().split()]

while True:
    command_input = input()

    if command_input == "end":
        break

    if command_input == "decrease":
        list_input = [el - 1 for el in list_input]
        continue
    else:
        command, index1, index2 = command_input.split()
        index_1 = int(index1)
        index_2 = int(index2)

    if command == "swap":
        list_input[index_1], list_input[index_2] = list_input[index_2], list_input[index_1]

    elif command == "multiply":
        number_1 = list_input[index_1]
        number_2 = list_input[index_2]
        multiply = number_1 * number_2
        list_input[index_1] = multiply

print(*list_input, sep=", ")
