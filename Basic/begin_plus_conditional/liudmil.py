budget = int(input())
season = input()
number_fisherman = int(input())

discount = 0
price = 0

if season == "Spring":
    if number_fisherman <= 6:
        discount = 3000 * 0.10
        price = 3000 - discount
    elif 7 < number_fisherman <= 11:
        discount = 3000 * 0.15
        price = 3000 - discount
    else:
        discount = 3000 * 0.25
        price = 3000 - discount

elif season == "Winter":
    if number_fisherman <= 6:
        discount = 2600 * 0.10
        price = 2600 - discount
    elif 7 < number_fisherman <= 11:
        discount = 2600 * 0.15
        price = 2600 - discount
    else:
        discount = 2600 * 0.25
        price = 2600 - discount

else:
    if number_fisherman <= 6:
        discount = 4200 * 0.10
        price = 4200 - discount
    elif 7 < number_fisherman <= 11:
        discount = 4200 * 0.15
        price = 4200 - discount
    else:
        discount = 4200 * 0.25
        price = 4200 - discount

if number_fisherman % 2 == 0 and season != "Autumn":
    discount = price * 0.05
    price = price - discount

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")