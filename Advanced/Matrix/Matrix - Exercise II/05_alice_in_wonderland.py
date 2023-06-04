def valid_index(r, c):
    return 0 <= r < n and 0 <= c < n


n = int(input())
field = []
alice_location = []
collected_tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    field.append(input().split())
    if "A" in field[row]:
        alice_location = [row, field[row].index("A")]

field[alice_location[0]][alice_location[1]] = "*"

while collected_tea < 10:
    direction = input()
    move_index = [alice_location[0] + directions[direction][0],
                  alice_location[1] + directions[direction][1]
                  ]

    if not valid_index(*move_index):
        break

    if field[move_index[0]][move_index[1]].isdigit():
        collected_tea += int(field[move_index[0]][move_index[1]])
    elif field[move_index[0]][move_index[1]] == "R":
        field[move_index[0]][move_index[1]] = "*"
        break

    field[move_index[0]][move_index[1]] = "*"
    alice_location = [move_index[0], move_index[1]]

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in field:
    print(*row)
