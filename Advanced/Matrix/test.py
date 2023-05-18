def turn_matrix_left(mat: list):
    result = []

    for col in range(len(mat) - 1, -1, -1):
        curr_list = []

        for row in range(len(mat)):
            curr_list.append(mat[row][col])

        result.append(curr_list)

    return result


matrix = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]

for _ in range(100):
    matrix = turn_matrix_left(matrix)
    print(matrix)