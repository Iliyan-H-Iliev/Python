price_by_product = {}
quantity_by_product = {}

while True:
    line = input()

    if line == "buy":
        break

    args = line.split()
    product_name = args[0]
    price = float(args[1])
    quantity = int(args[2])

    price_by_product[product_name] = price

    if product_name in quantity_by_product:
        quantity_by_product[product_name] += quantity
    else:
        quantity_by_product[product_name] = quantity

for product in price_by_product:
    print(f"{product} -> {price_by_product[product] * quantity_by_product[product]:.2f}")
