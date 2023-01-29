gifts_list = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command_list = command.split()

    if "OutOfStock" in command_list:
        for i in range(len(gifts_list)):
            if gifts_list[i] == command_list[1]:
                gifts_list[i] = "None"

    elif "Required" in command_list:
        if 0 <= int(command_list[2]) <= len(gifts_list) - 1:
            gifts_list[int(command_list[2])] = command_list[1]
        else:
            continue

    elif "JustInCase" in command_list:
        gifts_list[-1] = command_list[1]

for gift in gifts_list:
    if gift != "None":
        print(gift, end=" ")
