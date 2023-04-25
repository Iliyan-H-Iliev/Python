rows, cols = [int(x) for x in input().split(", ")]

matrix = []
col_1 = []
col_2 = []
best_result = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for i in range(rows - 1):
    for j in range(cols - 1):
        result = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j + 1]
        if result > best_result:
            best_result = result
            col_1 = [matrix[i][j], matrix[i][j + 1]]
            col_2 = [matrix[i + 1][j], matrix[i + 1][j + 1]]
print(*col_1, sep=" ")
print(*col_2, sep=" ")
print(best_result)
