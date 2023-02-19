item_list = input().split("|")

item_sum = 0

while True:
    command_input = input()

    if command_input == "Yohoho!":
        break

    command_arg = command_input.split()
    command = command_arg[0]

    if command == "Loot":
        for i in range(1, len(command_arg)):
            if command_arg[i] not in item_list:
                item_list.insert(0, command_arg[i])

    elif command == "Drop":
        index = int(command_arg[1])
        if 0 <= index < len(item_list):
            item = item_list[index]
            item_list.pop(index)
            item_list.append(item)

    elif command == "Steal":
        count = int(command_arg[1])

        if count > len(item_list):
            print(", ".join(item_list))
            item_list.clear()
            continue

        steal_items = []
        steal_index = []

        for i in range(len(item_list) - count, len(item_list)):
            steal_item = item_list[i]
            steal_items.append(steal_item)
            steal_index.append(i)
        print(", ".join(steal_items))
        for el in steal_items:
            item_list.remove(el)

for el in item_list:
    item_sum += len(el)

if item_list:
    print(f"Average treasure gain: {item_sum / len(item_list):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
