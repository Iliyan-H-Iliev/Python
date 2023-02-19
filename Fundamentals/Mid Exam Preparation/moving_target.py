def index_check(i, same_list):
    return 0 <= i < len(same_list)


targets = [int(x) for x in input().split()]

while True:

    command_input = input()

    if command_input == "End":
        break

    command_arg = command_input.split()
    command = command_arg[0]
    index = int(command_arg[1])
    value = int(command_arg[2])

    if command == "Shoot" and index_check(index, targets):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)

    elif command == "Add":
        if index_check(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike" and index_check(index, targets):
        if index_check(index - value, targets) and index_check(index + value, targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

print(*targets, sep="|")
