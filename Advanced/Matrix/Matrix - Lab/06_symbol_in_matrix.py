n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

looking_for = input()
founded = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] == looking_for:
            founded = (i, j)
            print(founded)
            break
    if founded:
        break
else:
    print(f"{looking_for} does not occur in the matrix")
