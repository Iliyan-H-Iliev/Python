from collections import deque
from datetime import datetime, timedelta

robots = {}
elements = deque()

for el in input().split(";"):
    key, value = el.split("-")
    robots[key] = [int(value), 0]

start_time = datetime.strptime(input(), "%H:%M:%S")


while True:
    data = input()

    if data == "End":
        break

    elements.append(data)

while elements:
    is_taken = False
    element = elements.popleft()
    start_time += timedelta(0, 1)

    for robot, time in robots.items():
        robots[robot][1] -= 1

    for robot, time in robots.items():
        if is_taken:
            continue

        if time[1] <= 0:
            time[1] = time[0]
            print(f"{robot} - {element} [{start_time.strftime('%H:%M:%S')}]")
            is_taken = True

    if not is_taken:
        elements.append(element)
