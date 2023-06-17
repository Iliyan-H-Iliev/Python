rows = int(input())
battle_field = []
sub_position = []
battle_cruisers = 3
hit_by_mine = 3

move = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(rows):
    battle_field.append(list(input()))
    if "S" in battle_field[i]:
        sub_position = [i, battle_field[i].index("S")]

while True:
    command = input()

    row = sub_position[0] + move[command][0]
    col = sub_position[1] + move[command][1]

    if battle_field[row][col] == "*":
        hit_by_mine -= 1
    elif battle_field[row][col] == "C":
        battle_cruisers -= 1

    battle_field[sub_position[0]][sub_position[1]] = "-"
    battle_field[row][col] = "S"
    sub_position = [row, col]

    if hit_by_mine == 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break
    elif battle_cruisers == 0:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

for el in battle_field:
    print(''.join(x for x in el))
