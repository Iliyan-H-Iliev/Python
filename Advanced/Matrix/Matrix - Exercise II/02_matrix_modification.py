def valid_index(idx_1, idx_2):
    return 0 <= idx_1 < n and 0 <= idx_2 < n


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command, *data = [x for x in input().split()]

    if command == "END":
        break

    data = [int(x) for x in data]

    if not valid_index(data[0], data[1]):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[data[0]][data[1]] += data[2]
    elif command == "Subtract":
        matrix[data[0]][data[1]] -= data[2]

[print(*el) for el in matrix]
