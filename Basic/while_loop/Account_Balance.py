total_money = 0

while True:
    increase = input()

    if increase == "NoMoreMoney":
        break

    money = float(increase)

    if money < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {money:.2f}")
    total_money += money


print(f"Total: {total_money:.2f}")
