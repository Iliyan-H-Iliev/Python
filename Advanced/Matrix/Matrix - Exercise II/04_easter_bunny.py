from sys import maxsize


def valid_index(r, c):
    return 0 <= r < n and 0 <= c < n


n = int(input())

max_eggs = -maxsize
field = []
collected_eggs_list = []
bunny_position = None
best_direction = None

for row in range(n):
    col = []
    for el in input().split():
        if el != "B" and el != "X":
            col.append(int(el))
        else:
            col.append(el)
    field.append(col)

    if "B" in field[row]:
        bunny_position = (row, field[row].index("B"))

direction = {
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, +1),
    "up": (-1, 0),
}

for k, v in direction.items():
    b_p = list(bunny_position)
    collected_eggs = 0
    eggs_position = []

    while valid_index(b_p[0] + v[0], b_p[1] + v[1]):
        b_p[0] += v[0]
        b_p[1] += v[1]
        el = field[b_p[0]][b_p[1]]

        if el == "X":
            break
        # elif el < 0:
        #     continue

        collected_eggs += el
        eggs_position.append([b_p[0], b_p[1]])

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        collected_eggs_list = eggs_position
        best_direction = k

print(best_direction)
print(*collected_eggs_list, sep="\n")
print(max_eggs)
