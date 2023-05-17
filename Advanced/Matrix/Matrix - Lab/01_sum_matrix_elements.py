rows, columns = (int(x) for x in input().split(", "))

matrix = []
sum_matrix = 0

# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    sum_matrix += sum(row)

print(sum_matrix)
print(matrix)
