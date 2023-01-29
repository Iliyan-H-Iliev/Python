movie_budget = float(input())
extras = int(input())
price_extras_clothing = float(input())

decor = movie_budget * 0.1

total_price_extras_clothing = extras * price_extras_clothing

if extras > 150:
    total_price_extras_clothing = total_price_extras_clothing - (total_price_extras_clothing * 0.1)

if movie_budget < decor + total_price_extras_clothing:
    print('Not enough money!')
    print(f'Wingard needs {(decor + total_price_extras_clothing) - movie_budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {movie_budget - (decor + total_price_extras_clothing):.2f} leva left.')
