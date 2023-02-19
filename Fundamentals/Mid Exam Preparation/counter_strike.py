energy = int(input())

won_battles = 0
is_won = True

while energy >= 0:

    command = input()

    if command == "End of battle":
        break

    distance = int(command)

    if energy < distance:
        is_won = False
        break

    energy -= distance
    won_battles += 1

    if won_battles % 3 == 0:
        energy += won_battles

if is_won:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
