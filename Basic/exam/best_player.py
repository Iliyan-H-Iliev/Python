best_player = ""
best_goals = 0


while True:
    player_name = input()

    if player_name == "END":
        break

    goals = int(input())

    if goals > best_goals:
        best_player = player_name
        best_goals = goals

    if goals >= 10:
        break

print(f"{best_player} is the best player!")

if best_goals >= 3:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")
