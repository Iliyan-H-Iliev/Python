goal = 10000
total_steps = 0

while total_steps < goal:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        total_steps += steps
        if total_steps < goal:
            print(f"{goal - total_steps} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{total_steps - goal} steps over the goal!")
        break

    total_steps += int(steps)


else:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
