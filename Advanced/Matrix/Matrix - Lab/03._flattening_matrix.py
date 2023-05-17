n = int(input())

flatted_matrix = []

for _ in range(n):
    flatted_matrix.extend([int(x) for x in input().split(", ")])

    # inner_list = [int(x) for x in input().split(", ")]
    # for el in inner_list:
    #     flatted_matrix.append(el)

print(flatted_matrix)
