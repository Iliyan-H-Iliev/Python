nylon = int(input()) + 2
paint = int(input())
thinner = int(input())
working_hours = int(input())

nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
plastic_bags_price = 0.4
paint += paint * 0.1

materials_price = \
    (nylon * nylon_price) + \
    (paint * paint_price) + \
    (thinner * thinner_price) + plastic_bags_price

working_hours_price = working_hours * (materials_price * 0.3)

total_price = materials_price + working_hours_price

print(total_price)
