country_names = input().split(", ")
capital_cities = input().split(", ")

country_capital = {k: v for k, v in zip(country_names, capital_cities)}

for key, value in country_capital.items():
    print(f"{key} -> {value}")
