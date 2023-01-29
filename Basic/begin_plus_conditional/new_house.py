type_flowers = input()
count_flowers = int(input())
budget = int(input())

price = 0

rose = 5
dahlia = 3.8
tulip = 2.8
narcissus = 3
gladiolus = 2.5

if type_flowers == 'Roses':
    price = count_flowers * rose
    if count_flowers > 80:
        price *= 0.9
elif type_flowers == 'Dahlias':
    price = count_flowers * dahlia
    if count_flowers > 90:
        price *= 0.85
elif type_flowers == 'Tulips':
    price = count_flowers * tulip
    if count_flowers > 80:
        price *= 0.85
elif type_flowers == 'Narcissus':
    price = count_flowers * narcissus
    if count_flowers < 120:
        price *= 1.15
elif type_flowers == 'Gladiolus':
    price = count_flowers * gladiolus
    if count_flowers < 80:
        price *= 1.2

if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
