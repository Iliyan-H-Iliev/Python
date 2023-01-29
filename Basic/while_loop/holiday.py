holiday_price = float(input())
current_money = float(input())

spend_days = 0
total_days = 0

while holiday_price > current_money:
    action = input()
    money = float(input())
    total_days += 1

    if action == "spend":
        spend_days += 1
        current_money -= money
        if current_money < 0:
            current_money = 0

    elif action == "save":
        spend_days = 0
        current_money += money

    if spend_days >= 5:
        print("You can't save the money.")
        print(total_days)
        break


else:
    print(f"You saved the money for {total_days} days.")
