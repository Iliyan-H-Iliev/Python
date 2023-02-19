def item_in_items(i, some_list):
    return i in some_list


items_list = input().split(", ")

while True:

    command_input = input()

    if command_input == "Craft!":
        break

    command_arg = command_input.split(" - ")
    command = command_arg[0]
    item = command_arg[1]

    if command == "Collect" and not item_in_items(item, items_list):
        items_list.append(item)

    elif command == "Drop" and item_in_items(item, items_list):
        items_list.remove(item)

    elif command == "Combine Items":
        item_arg = item.split(":")
        old_item = item_arg[0]
        new_item = item_arg[1]
        if item_in_items(old_item, items_list):
            old_item_index = items_list.index(old_item)
            items_list.insert(old_item_index + 1, new_item)

    elif command == "Renew" and item_in_items(item, items_list):
        items_list.remove(item)
        items_list.append(item)

print(", ".join(items_list))
