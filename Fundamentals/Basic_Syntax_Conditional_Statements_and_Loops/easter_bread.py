budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
liter_of_milk = flour_price * 1.25
quarter_liter_milk = liter_of_milk / 4

current_bread_count = 0
colored_eggs_count = 0
lost_eggs = 0

bread_price = flour_price + eggs_price + quarter_liter_milk

while True:
    if budget - bread_price < 0:
        break

    current_bread_count += 1
    budget -= bread_price
    colored_eggs_count += 3

    if current_bread_count % 3 == 0:
        lost_eggs += current_bread_count - 2

total_colored_eggs = colored_eggs_count - lost_eggs

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {total_colored_eggs}"
      f" eggs and {budget:.2f}BGN left.")
