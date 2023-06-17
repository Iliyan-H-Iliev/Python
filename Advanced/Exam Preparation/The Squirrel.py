def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < rows


rows = int(input())
commands = input().split(", ")
field = []
squirrels_position = []
hazelnut = 3
text = ""

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(rows):
    field.append(list(input()))
    if "s" in field[i]:
        squirrels_position = [i, field[i].index("s")]

for command in commands:
    new_position = [squirrels_position[0] + movements[command][0],
                    squirrels_position[1] + movements[command][1],
                    ]

    if not valid_index(*new_position):
        text = "The squirrel is out of the field."
        break

    if field[new_position[0]][new_position[1]] == "t":
        text = "Unfortunately, the squirrel stepped on a trap..."
        break

    if field[new_position[0]][new_position[1]] == "h":
        hazelnut -= 1
        if hazelnut == 0:
            text = "Good job! You have collected all hazelnuts!"
            break

    field[squirrels_position[0]][squirrels_position[1]] = "*"
    field[new_position[0]][new_position[1]] = "s"
    squirrels_position = [*new_position]
else:
    if hazelnut > 0:
        text = "There are more hazelnuts to collect."

print(text)
print(f"Hazelnuts collected: {3 - hazelnut}")
