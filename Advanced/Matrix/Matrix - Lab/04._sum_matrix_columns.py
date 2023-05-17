rows, cols = (int(x) for x in input().split(", "))

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for j in range(cols):
    row_sum = 0
    for i in range(rows):
        row_sum += matrix[i][j]

    print(row_sum)
