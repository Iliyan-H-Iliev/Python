from math import floor

count_tournament = int(input())
points = int(input())

total_points = 0
win = 0

for i in range(0, count_tournament):
    stage = input()

    if stage == "W":
        total_points += 2000
        win += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

print(f"Final points: {total_points + points}")
print(f"Average points: {floor(total_points / count_tournament)}")
print(f"{(win / count_tournament) * 100:.2f}%")
