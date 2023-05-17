from sys import maxsize
rows, cols = [int(x) for x in input().split()]

winner_matrix = []
best_result = -maxsize

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for i in range(rows - 2):
    for j in range(cols - 2):
        small_matrix = []
        result = 0
        for k in range(3):
            result += sum(matrix[i + k][j:j + 3])
            small_matrix.append(matrix[i + k][j:j + 3])

        if abs(result) >= best_result:
            best_result = result
            winner_matrix = small_matrix.copy()

print(f"Sum = {best_result}")
for el in winner_matrix:
    print(*el, sep=" ")
