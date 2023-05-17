n = int(input())

primary = []
secondary = []

for i in range(n):
    n -= 1
    inner_list = [int(x) for x in input().split()]
    primary.append(inner_list[i])
    secondary.append(inner_list[n])

print(abs(sum(primary) - sum(secondary)))
