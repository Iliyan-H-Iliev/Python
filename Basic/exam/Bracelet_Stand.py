days_money = float(input())
sell_money = float(input())
total_expenses = float(input())
gift_price = float(input())

total_saved_money = (5 * days_money + 5 * sell_money) - total_expenses

if total_saved_money >= gift_price:
    print(f"Profit: {total_saved_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - total_saved_money:.2f} BGN.")
