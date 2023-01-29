command_list = list(input().split("|"))
energy = 100
coins = 100

is_day_completed = True

for el in command_list:
    current_command = el.split("-")
    command = str(current_command[0])
    value = int(current_command[1])

    if command == "rest":
        if energy + value > 100:
            needed_energy = 100 - energy
            print(f"You gained {needed_energy} energy.")
            energy = 100
        elif energy + value <= 100:
            print(f"You gained {value} energy.")
            energy += value
        print(f"Current energy: {energy}.")

    elif command == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            if energy + 50 <= 100:
                energy += 50
            else:
                energy = 100
            print(f"You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {command}.")
        else:
            is_day_completed = False
            print(f"Closed! Cannot afford {command}.")
            break

if is_day_completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
