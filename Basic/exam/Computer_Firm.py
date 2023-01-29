count_computer_models = int(input())

total_sells = 0
rating = 0

for _ in range(count_computer_models):
    price_and_rating = int(input())

    if price_and_rating % 10 == 2:
        rating += 2

    elif price_and_rating % 10 == 3:
        rating += 3
        total_sells += (price_and_rating // 10) * 0.5
    elif price_and_rating % 10 == 4:
        rating += 4
        total_sells += (price_and_rating // 10) * 0.7
    elif price_and_rating % 10 == 5:
        rating += 5
        total_sells += (price_and_rating // 10) * 0.85
    elif price_and_rating % 10 == 6:
        rating += 6
        total_sells += (price_and_rating // 10)

print(f"{total_sells:.2f}")
print(f"{rating / count_computer_models:.2f}")
