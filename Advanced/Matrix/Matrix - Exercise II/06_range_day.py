def validate_index(id_1, id_2):
    return 0 <= id_1 < ROW and 0 <= id_2 < ROW


ROW = 5
matrix = []
start_position = []

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(ROW):
    matrix.append([xinput().split()])
    for j in range(ROW):
        if matrix[i][j] == "A":
            start_position = [i, j]

