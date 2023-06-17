
rows = int(input())
car_number = input()
passed_kilometers = 0
car_position = [0, 0]
tunnel = []
route = []

move = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(rows):
    route.append(input().split())
    if "T" in route[i]:
        for t in range(rows):
            if route[i][t] == "T":
                tunnel.append([i, t])


while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    row = car_position[0] + move[command][0]
    col = car_position[1] + move[command][1]

    if route[row][col] == "T":
        for el in tunnel:
            if el != [row, col]:
                row = el[0]
                col = el[1]
                passed_kilometers += 20
                route[tunnel[0][0]][tunnel[0][1]] = "."
                route[tunnel[1][0]][tunnel[1][1]] = "."

    car_position = [row, col]
    passed_kilometers += 10

    if route[row][col] == "F":
        print(f"Racing car {car_number} finished the stage!")
        break

route[car_position[0]][car_position[1]] = "C"

print(f"Distance covered {passed_kilometers} km.")
for el in route:
    print(''.join(x for x in el))
