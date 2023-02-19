def extra_experience(ex_per_bat, percent):
    result = ex_per_bat * percent
    return result


needed_experience = float(input())
count_of_battles = int(input())

battle_count = 0

for i in range(1, count_of_battles + 1):
    experience_per_battle = float(input())

    needed_experience -= experience_per_battle
    battle_count += 1

    # check is only 15 or 3 and 5 + 15
    if i % 15 == 0:
        needed_experience -= extra_experience(experience_per_battle, 0.05)
        continue

    if i % 3 == 0:
        needed_experience -= extra_experience(experience_per_battle, 0.15)
    elif i % 5 == 0:
        needed_experience += extra_experience(experience_per_battle, 0.1)

    if needed_experience <= 0:
        break

if needed_experience <= 0:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")
