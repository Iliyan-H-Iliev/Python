from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes = 0

while chocolates and cups_of_milk and milkshakes != 5:
    chocolate = chocolates.pop()
    milk_cup = cups_of_milk.popleft()

    if chocolate <= 0 < milk_cup:
        cups_of_milk.appendleft(milk_cup)
        continue
    elif milk_cup <= 0 < chocolate:
        chocolates.append(chocolate)
        continue
    elif chocolate <= 0 and milk_cup <= 0:
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        cups_of_milk.append(milk_cup)
        chocolates.append(chocolate - 5)

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
