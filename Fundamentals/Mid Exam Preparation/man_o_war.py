def is_valid(ind, some_list):
    return 0 <= ind < len(some_list)


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health = int(input())

is_play = True

while is_play:

    commands = input()

    if commands == "Retire":
        break

    command_args = commands.split()
    command = command_args[0]

    if command == "Fire":
        index = int(command_args[1])
        damage = int(command_args[2])

        if is_valid(index, war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                is_play = False
                print("You won! The enemy ship has sunken.")

    elif command == "Defend":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        damage = int(command_args[3])

        if is_valid(start_index, pirate_ship) and is_valid(end_index, pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    is_play = False
                    print("You lost! The pirate ship has sunken.")
                    break

    elif command == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if is_valid(index, pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif command == "Status":
        count = 0
        for el in pirate_ship:
            if el < max_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")


if is_play:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
