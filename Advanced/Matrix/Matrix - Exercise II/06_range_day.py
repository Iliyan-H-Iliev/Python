def validate_index(id_1, id_2):
    return 0 <= id_1 < ROW and 0 <= id_2 < ROW


def move(direction, steps):
    new_position = [
        start_position[0] + movement[direction][0] * steps,
        start_position[1] + movement[direction][1] * steps,
    ]
    if validate_index(*new_position) and matrix[new_position[0]][new_position[1]] != "x":
        return new_position
    return start_position


def shoot(direction):
    for m in range(1, ROW):
        shoot_position = [
            start_position[0] + movement[direction][0] * m,
            start_position[1] + movement[direction][1] * m,
        ]

        if validate_index(*shoot_position):
            if matrix[shoot_position[0]][shoot_position[1]] == "x":
                return shoot_position

        else:
            return False


ROW = 5
matrix = []
start_position = []
targets = 0
shoot_targets = []

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(ROW):
    matrix.append(input().split())
    for j in range(ROW):
        if matrix[i][j] == "A":
            start_position = [i, j]
        elif matrix[i][j] == "x":
            targets += 1

for _ in range(int(input())):
    command, *data = input().split()

    if command == "move":
        start_position = move(data[0], int(data[1]))
    elif command == "shoot":
        shoot_data = shoot(*data)
        if shoot_data:
            targets -= 1
            shoot_targets.append(shoot_data)
            matrix[shoot_data[0]][shoot_data[1]] = "."

    if targets == 0:
        print(f"Training completed! All {len(shoot_targets)} targets hit.")
        break
else:
    print(f"Training not completed! {targets} targets left.")

print(*shoot_targets, sep="\n")
