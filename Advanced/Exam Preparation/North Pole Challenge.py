def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < cols


def checking(r, c):
    if field[r][c] == "D":
        return "Christmas decorations", 1
    elif field[r][c] == "C":
        return "Cookies", 1
    elif field[r][c] == "G":
        return "Gifts", 1
    else:
        return None


def move(com, step):
    if com == "up":
        return -1, movement[command][0] * step - 1, -1
    elif com == "down":
        return 1, movement[command][0] * step + 1
    elif com == "left":
        return -1, movement[command][1] * step - 1, -1
    elif com == "right":
        return 1, movement[command][1] * step + 1


rows, cols = [int(x) for x in input().split(", ")]

is_all_collected = False
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

while True:
    command, *data = input().split("-")

    if command == "End":
        break

    steps = int(data[0])

    new_location_row = my_location[0] + movement[command][0] * steps
    new_location_col = my_location[1] + movement[command][1] * steps

    if my_location[0] - new_location_row != 0:

        for i in range(*move(command, steps)):
            old = [my_location[0], my_location[1]]
            my_location = [my_location[0] + int(i / abs(i)), my_location[1]]
            if not valid_index(my_location[0], my_location[1]):
                if command == "up":
                    my_location = [rows - 1, my_location[1]]
                elif command == "down":
                    my_location = [0, my_location[1]]
            item = checking(*my_location)
            if item:
                collected_items[item[0]] += item[1]
                all_items -= 1
            field[old[0]][old[1]] = "x"
            field[my_location[0]][my_location[1]] = "Y"
            if all_items == 0:
                is_all_collected = True
                break

    elif my_location[1] - new_location_col != 0:
        for i in range(*move(command, steps)):
            old = [my_location[0], my_location[1]]
            my_location = [my_location[0], my_location[1] + int(i / abs(i))]
            if not valid_index(my_location[0], my_location[1]):
                if command == "left":
                    my_location = [my_location[0], cols - 1]
                elif command == "right":
                    my_location = [my_location[0], 0]
            item = checking(*my_location)
            if item:
                collected_items[item[0]] += item[1]
                all_items -= 1
            field[old[0]][old[1]] = "x"
            field[my_location[0]][my_location[1]] = "Y"
            if all_items == 0:
                is_all_collected = True
                break

    if is_all_collected:
        break


if is_all_collected:
    print("Merry Christmas!")

print("You've collected:")
for item, value in collected_items.items():
    print(f"- {value} {item}")

for el in field:
    print(" ".join(x for x in el))
