matrix = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]


def rotate_matrix_left(matrix_l, times):
    r = len(matrix_l)

    for _ in range(times):
        new_matrix = [list("*" * r) for _ in range(r)]
        for i in range(r):
            for j in range(r):
                el = matrix_l[i][j]
                new_matrix[r - 1 - j][i] = el
        matrix_l = new_matrix.copy()
    return matrix_l


def rotate_matrix_right(matrix_r, times):
    r = len(matrix_r)

    for _ in range(times):
        new_matrix = [list("*" * r) for _ in range(r)]
        for i in range(r):
            for j in range(r):
                el = matrix_r[i][j]
                new_matrix[j][r - 1 - i] = el
        matrix_r = new_matrix.copy()
    return matrix_r


print(rotate_matrix_left(matrix, 1))
print(rotate_matrix_left(matrix, 2))
print(rotate_matrix_left(matrix, 3))
print(rotate_matrix_left(matrix, 4))
print()
print(rotate_matrix_right(matrix, 1))
print(rotate_matrix_right(matrix, 2))
print(rotate_matrix_right(matrix, 3))
print(rotate_matrix_right(matrix, 4))
