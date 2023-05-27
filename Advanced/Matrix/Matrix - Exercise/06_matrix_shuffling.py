def coordinates_validator(coordinates_list):
    return len(coordinates_list) == 4 and \
        {coordinates_list[0], coordinates_list[2]}.issubset(valid_index_row) and \
        {coordinates_list[1], coordinates_list[3]}.issubset(valid_index_col)


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()]for _ in range(rows)]

valid_index_row = range(rows)
valid_index_col = range(cols)

while True:
    command, *current_c = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    if command == "swap" and coordinates_validator(current_c):
        matrix[current_c[0]][current_c[1]], matrix[current_c[2]][current_c[3]] = \
            matrix[current_c[2]][current_c[3]], matrix[current_c[0]][current_c[1]]
        for el in matrix:
            print(*el)
    else:
        print("Invalid input!")
