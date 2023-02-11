def merge_str(some_list, start, end):
    result = "".join(some_list[x] for x in range(start, end + 1))
    return result


def divide_word(word, parts):
    result = []
    partition_size = len(word) // parts
    position = 0
    for i in range(parts - 1):
        result.append(word[position:position + partition_size])
        position += partition_size
    result.append(word[position:])
    return result


string_list_input = input().split()

while True:

    command_input = input()

    if command_input == "3:1":
        break

    command, first_number, second_number = command_input.split()

    if command == "merge":
        start_index = max(int(first_number), 0)
        end_index = min(int(second_number), len(string_list_input) - 1)
        merge_string = merge_str(string_list_input, start_index, end_index)
        string_list_input = string_list_input[:start_index] + [merge_string] + string_list_input[end_index + 1:]

    if command == "divide":
        index = int(first_number)
        partitions = int(second_number)
        list_of_divided_string = divide_word(string_list_input[index], partitions)
        string_list_input = string_list_input[:index] + list_of_divided_string + string_list_input[index + 1:]

print(*string_list_input)