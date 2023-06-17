from collections import deque

food = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])
mountain_peaks = deque([["Vihren", 80],
                        ["Kutelo", 90],
                        ["Banski Suhodol", 100],
                        ["Polezhan", 60],
                        ["Kamenitza", 70],
                        ])

mountain = []

for _ in range(7):
    current_food = food.pop()
    current_stamina = stamina.popleft()

    power = current_food + current_stamina

    if power >= mountain_peaks[0][1]:
        mountain.append(mountain_peaks.popleft()[0])

    if len(mountain) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if mountain:
    print("Conquered peaks:")
    print(*mountain, sep="\n")
