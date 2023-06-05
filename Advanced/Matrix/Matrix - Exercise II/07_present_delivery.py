def validate_index(id_1, id_2):
    return 0 <= id_1 < rows and 0 <= id_2 < rows


def move(direction):
    new_position = [
        santa_location[0] + movement[direction][0],
        santa_location[1] + movement[direction][1],
    ]
    if validate_index(*new_position):
        return new_position
    return santa_location


count_presents = int(input())
rows = int(input())

neighborhood = []
santa_location = []
good_kids = 0
happy_kids = 0
movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),


}

for i in range(rows):
    neighborhood.append(input().split())
    for j in range(rows):
        if neighborhood[i][j] == "S":
            santa_location = [i, j]
        elif neighborhood[i][j] == "V":
            good_kids += 1


while count_presents > 0:
    command = input()

    if command == "Christmas morning":
        break

    new_santa_location = move(command)
    neighborhood[santa_location[0]][santa_location[1]] = "-"
    santa_location = [new_santa_location[0], new_santa_location[1]]

    if neighborhood[santa_location[0]][santa_location[1]] == "V":
        count_presents -= 1
        good_kids -= 1
        happy_kids += 1

    elif neighborhood[santa_location[0]][santa_location[1]] == "C":
        for direct in movement.keys():
            check_location = move(direct)
            if neighborhood[check_location[0]][check_location[1]].isalpha():

                if neighborhood[check_location[0]][check_location[1]] == "V":
                    good_kids -= 1
                    happy_kids += 1

                count_presents -= 1
                neighborhood[check_location[0]][check_location[1]] = "-"

                if count_presents == 0:
                    break

    neighborhood[new_santa_location[0]][new_santa_location[1]] = "S"

if count_presents == 0 and good_kids > 0:
    print("Santa ran out of presents!")


print(*[' '.join(line) for line in neighborhood], sep='\n')

if good_kids == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids} nice kid/s.")
