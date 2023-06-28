def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < cols


def move_mouse(old_r, old_c, new_r, new_c):
    field[old_r][old_c] = "*"
    field[new_r][new_c] = "M"


rows, cols = [int(x) for x in input().split(",")]

field = []
mouse_position = []
cheese = 0

directions = {
    "up": lambda r, c: [(r - 1), c],
    "down": lambda r, c: [(r + 1), c],
    "left": lambda r, c: [r, (c - 1)],
    "right": lambda r, c: [r, (c + 1)],

}

for i in range(rows):
    field.append(list(input()))
    if "M" in field[i]:
        mouse_position = [i, field[i].index("M")]
    cheese += field[i].count("C")

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    new_position = directions[command](*mouse_position)

    if not valid_index(*new_position):
        print("No more cheese for tonight!")
        break
    elif field[new_position[0]][new_position[1]] == "T":
        print("Mouse is trapped!")
        move_mouse(*mouse_position, *new_position)
        break
    elif field[new_position[0]][new_position[1]] == "C":
        cheese -= 1
        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            move_mouse(*mouse_position, *new_position)
            break
    elif field[new_position[0]][new_position[1]] == "@":
        continue


    move_mouse(*mouse_position, *new_position)
    mouse_position = [new_position[0], new_position[1]]

for row in field:
    print("".join(x for x in row))
