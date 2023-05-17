n = int(input())

primary_diagonal_sum = 0


for i in range(n):
    inner_list = [int(x) for x in input().split()]
    primary_diagonal_sum += inner_list[i]

print(primary_diagonal_sum)
