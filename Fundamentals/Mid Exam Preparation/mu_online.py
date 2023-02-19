dungeons_rooms = input().split("|")
health = 100
bitcoins = 0

is_alive = True

for i in range(len(dungeons_rooms)):

    command_arg = dungeons_rooms[i].split()
    command = command_arg[0]
    points = int(command_arg[1])

    if command == "potion":
        current_health = health
        health += points
        amount = points
        if health > 100:
            health = 100
            amount = 100 - current_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        health -= points
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            is_alive = False
            break

if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
