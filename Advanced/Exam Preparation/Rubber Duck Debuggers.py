from collections import deque

rubber_duck = {
    "Darth Vader Ducky": [60, 0],
    "Thor Ducky": [120, 0],
    "Big Blue Rubber Ducky": [180, 0],
    "Small Yellow Rubber Ducky": [240, 0],

}

programmers_time = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])

while programmers_time and number_of_tasks:
    current_prog_time = programmers_time.popleft()
    current_task = number_of_tasks.pop()

    calc_time = current_prog_time * current_task

    if calc_time > 240:
        programmers_time.append(current_prog_time)
        number_of_tasks.append(current_task - 2)
    else:
        for duck, time in rubber_duck.items():
            if calc_time <= time[0]:
                rubber_duck[duck][1] += 1
                break

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in rubber_duck.items():
    print(f"{duck}: {count[1]}")
