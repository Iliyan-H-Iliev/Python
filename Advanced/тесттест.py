def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < cols


def checking(r, c):
    if field[r][c] == "D":
        return "Christmas decorations"
    elif field[r][c] == "C":
        return "Cookies"
    elif field[r][c] == "G":
        return "Gifts"
    else:
        return None


def move(com):
    if com == "up" or com == "left":
        return -1
    elif com == "down" or com == "right":
        return 1


rows, cols = [int(x) for x in input().split(", ")]

field = []
my_location = []
all_items = 0

collected_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(rows):
    field.append(input().split())
    if "Y" in field[i]:
        my_location = [i, field[i].index("Y")]
    all_items += field[i].count("G")
    all_items += field[i].count("C")
    all_items += field[i].count("D")

while all_items > 0:
    command, *data = input().split("-")

    if command == "End":
        break

    steps = int(data[0])

    for i in range(steps):
        field[my_location[0]][my_location[1]] = "x"

        if command == "up" or command == "down":
            my_location = [my_location[0] + move(command), my_location[1]]
            if not valid_index(my_location[0], my_location[1]):
                if command == "up":
                    my_location = [rows - 1, my_location[1]]
                elif command == "down":
                    my_location = [0, my_location[1]]
        elif command == "left" or command == "right":
            my_location = [my_location[0], my_location[1] + move(command)]
            if not valid_index(my_location[0], my_location[1]):
                if command == "left":
                    my_location = [my_location[0], cols - 1]
                elif command == "right":
                    my_location = [my_location[0], 0]

        item = checking(*my_location)
        if item:
            collected_items[item] += 1
            all_items -= 1

        field[my_location[0]][my_location[1]] = "Y"
        if all_items == 0:
            break

print("Merry Christmas!") if all_items == 0 else None

print("You've collected:")
for item, value in collected_items.items():
    print(f"- {value} {item}")

for el in field:
    print(" ".join(x for x in el))
