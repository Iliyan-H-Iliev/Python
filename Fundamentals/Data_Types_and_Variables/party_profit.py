from math import floor
group_size = int(input())
days = int(input())

coins = 0

for d in range(1, days + 1):

    if d % 10 == 0:
        group_size -= 2
    if d % 15 == 0:
        group_size += 5

    coins += 50 - (group_size * 2)

    if d % 3 == 0:
        coins -= group_size * 3
    if d % 5 == 0:
        coins += group_size * 20
        if d % 3 == 0:
            coins -= group_size * 2

print(f"{group_size} companions received {floor(coins / group_size)} coins each.")
