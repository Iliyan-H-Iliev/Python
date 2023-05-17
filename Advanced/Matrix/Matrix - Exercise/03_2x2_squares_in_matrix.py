rows, cols = (int(x) for x in input().split())

counter = 0

matrix = [[x for x in input().split()] for _ in range(rows)]

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j] \
                and matrix[i][j] == matrix[i + 1][j + 1]:
            counter += 1

print(counter)
