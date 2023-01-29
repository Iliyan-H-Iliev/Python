number_of_orders = int(input())
total_price = 0

for _ in range(0, number_of_orders):
    order_price = 0
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2000:
        order_price = days * capsule_per_day * price_per_capsule
        total_price += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")
    else:
        continue

print(f"Total: ${total_price:.2f}")
