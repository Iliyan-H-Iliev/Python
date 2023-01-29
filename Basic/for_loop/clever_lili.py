lili_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

age_count = 0
money = 0


for i in range(1, lili_age + 1):
    if i % 2 == 0:
        age_count += 1
        money += age_count * 10 - 1
    else:
        money += toy_price

if money >= washing_machine_price:
    print(f"Yes! {money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money:.2f}")
