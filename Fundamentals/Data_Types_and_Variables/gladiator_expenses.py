lost_fight = int(input())
helm_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_broken_count = 0
for i in range(1, lost_fight + 1):

    if i % 2 == 0:
        expenses += helm_price
    if i % 3 == 0:
        expenses += sword_price
        if i % 2 == 0:
            shield_broken_count += 1
            expenses += shield_price
            if shield_broken_count % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
