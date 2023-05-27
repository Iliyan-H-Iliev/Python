def valid_idx(row, col):
    return 0 <= row < 5 and 0 <= col < 5


matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = ()
for rows in range(5):
    matrix.append(input().split())
    for cols in range(5):
        if matrix[rows][cols] == "A":
            start = (rows, cols)

for _ in range(int(input())):
    command = input().split()

    if command[0] == "move":
        new_rows, new_cols = (directions[command[1]][0] * int(command[3])) + start[0], (
                    directions[command[1]][1] * int(command[3])) + start[1]

        if matrix[new_rows][new_cols] != "." or not valid_idx(new_rows, new_cols):
            new_rows, new_cols = (directions[command[1]][0] * int(command[3])) - start[0], (
                        directions[command[1]][1] * int(command[3])) - start[1]
            continue
