budget = int(input())
season = input()
fishers = int(input())

ship_price = 0

if season == "Spring":
    ship_price = 3000
    if fishers <= 6:
        ship_price *= 0.9
    elif 7 <= fishers <= 11:
       ship_price *= 0.85
    else:
        ship_price *= 0.75

elif season == "Winter":
    ship_price = 2600
    if fishers <= 6:
        ship_price *= 0.9
    elif 7 <= fishers <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75
else:
    ship_price = 4200
    if fishers <= 6:
        ship_price *= 0.9
    elif 7 <= fishers <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75

if fishers % 2 == 0 and not season == "Autumn":
    ship_price *= 0.95

if budget >= ship_price:
    print(f'Yes! You have {budget - ship_price:.2f} leva left.')
else:
    print(f"Not enough money! You need {ship_price - budget:.2f} leva.")
