def index_validation(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(x) for x in input().split()]

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

playground = []
my_position = []
moves_count = 0
touch_count = 0

for i in range(rows):
    playground.append(input().split())
    if "B" in playground[i]:
        my_position = [i, playground[i].index("B")]

while True:
    command = input()

    if command == "Finish":
        break

    new_pos_row = my_position[0] + movement[command][0]
    new_pos_col = my_position[1] + movement[command][1]

    if not index_validation(new_pos_row, new_pos_col)\
            or playground[new_pos_row][new_pos_col] == "O":
        continue

    if playground[new_pos_row][new_pos_col] == "P":
        touch_count += 1

    playground[my_position[0]][my_position[1]] = "-"
    playground[new_pos_row][new_pos_col] = "B"
    my_position = [new_pos_row, new_pos_col]
    moves_count +=1

    if touch_count == 3:
        break

print("Game over!")
print(f"Touched opponents: {touch_count} Moves made: {moves_count}")
