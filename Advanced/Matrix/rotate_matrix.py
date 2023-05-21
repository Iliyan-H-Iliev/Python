n = int(input("n = "))
print("input the matrix")
matrix = [[int(x) for x in input().split()] for _ in range(n)]
rotate = input("L - R - ")
times = int(input("How meny times you want to rotate the matrix - "))

for _ in range(times):
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            el = matrix[i][j]
            if rotate == "L":
                new_matrix[n - 1 - j][i] = el
            else:
                new_matrix[j][n - 1 - i] = el

    matrix = new_matrix.copy()

print(matrix)