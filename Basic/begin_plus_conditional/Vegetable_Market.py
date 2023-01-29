price_vegetables = float(input())
price_fruits = float(input())
weight_vegetable = int(input())
weight_fruits = int(input())

total_price = price_vegetables * weight_vegetable + price_fruits * weight_fruits
euro_price = total_price / 1.94

print(f'{euro_price:.2f}')
