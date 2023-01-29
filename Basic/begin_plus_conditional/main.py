area = float(input())

full_price = area * 7.61
discount = full_price * 0.18
discount_price = full_price - discount

print(f'The final price is: {discount_price} lv.')
print(f"The discount is: {discount} lv.")