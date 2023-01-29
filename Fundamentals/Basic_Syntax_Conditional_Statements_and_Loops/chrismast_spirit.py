decoration_quantity = int(input())
day_left_to_christmas = int(input())

christmas_spirit = 0
spend_money = 0

for i in range(1, day_left_to_christmas + 1):

    if i % 11 == 0:
        decoration_quantity += 2

    if i % 2 == 0:
        spend_money += decoration_quantity * 2
        christmas_spirit += 5

    if i % 3 == 0:
        spend_money += decoration_quantity * 8
        christmas_spirit += 13

    if i % 5 == 0:
        spend_money += decoration_quantity * 15
        christmas_spirit += 17

    if i % 15 == 0:
        christmas_spirit += 30

    if i % 10 == 0:
        spend_money += 23
        christmas_spirit -= 20

if day_left_to_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {spend_money}")
print(f"Total spirit: {christmas_spirit}")
