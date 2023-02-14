shopping_list = input().split("!")

while True:
    commands = input()

    if commands == "Go Shopping!":
        break

    command_args = commands.split()
    command = command_args[0]
    item = command_args[1]

    if item not in shopping_list:
        if command == "Urgent":
            shopping_list.insert(0, item)
    else:
        if command == "Unnecessary":
            shopping_list.remove(item)

        elif command == "Correct":
            new_item = command_args[2]
            item_index = shopping_list.index(item)
            shopping_list.remove(item)
            shopping_list.insert(item_index, new_item)

        elif command == "Rearrange":
            shopping_list.remove(item)
            shopping_list.append(item)

print(", ".join(shopping_list))
