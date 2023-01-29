while True:
    destination = input()

    if destination == "End":
        break

    holiday_price = float(input())
    saved_money = 0

    while saved_money < holiday_price:
        money = float(input())
        saved_money += money
    else:
        print(f"Going to {destination}!")
