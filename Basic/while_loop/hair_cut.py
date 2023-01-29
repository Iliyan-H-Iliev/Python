target = int(input())

money = 0

is_target = False

while True:
    if money >= target:
        is_target = True
        break

    type_service = input()

    if type_service == "closed":
        break

    service = input()

    if type_service == "haircut":
        if service == "mens":
            money += 15
        elif service == "ladies":
            money += 20
        elif service == "kids":
            money += 10

    elif type_service == "color":
        if service == "touch up":
            money += 20
        elif service == "full color":
            money += 30

if is_target:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target - money}lv. more.")

print(f"Earned money: {money}lv.")
