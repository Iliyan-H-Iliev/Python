holiday_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
discount = 0

puzzles_price = 2.6
dolls_price = 3
bears_price = 4.1
minions_price = 8.2
trucks_price = 2

total_toys = puzzles + dolls + bears + minions + trucks

total_toys_price = puzzles * puzzles_price + \
    dolls * dolls_price + bears * bears_price + \
    minions * minions_price + trucks * trucks_price

if total_toys >= 50:
    discount = total_toys_price * 0.25

rent = (total_toys_price - discount) * 0.1

profit = total_toys_price - discount - rent

if profit >= holiday_price:
    print(f'Yes! {profit - holiday_price:.2f} lv left.')
else:
    print(f'Not enough money! {holiday_price - profit:.2f} lv needed.')
