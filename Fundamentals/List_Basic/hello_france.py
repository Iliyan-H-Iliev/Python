item_list = list(input().split("|"))
budget = float(input())

sold_items_price = []
profit = 0

for el in item_list:
    current_element = el.split("->")
    current_price = float(current_element[1])
    is_ok = False

    if budget < current_price:
        continue

    if "Clothes" in current_element and 0 <= current_price <= 50:
        is_ok = True
    elif "Shoes" in current_element and 0 <= current_price <= 35:
        is_ok = True
    elif "Accessories" in current_element and 0 <= current_price <= 20.50:
        is_ok = True

    if is_ok:
        budget -= current_price
        current_profit = (current_price * 0.4)
        profit += current_profit
        sold_items_price.append(current_price + current_profit)

for price in sold_items_price:
    print(f"{price:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")

if sum(sold_items_price) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
