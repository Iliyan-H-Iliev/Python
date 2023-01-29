actor_name = input()
first_points = float(input())
jury = int(input())

total_point = 0

for i in range(1, jury + 1):
    name_jury = input()
    points = float(input())

    total_point += ((len(name_jury) * points) / 2)

    if first_points + total_point >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {first_points + total_point:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - (first_points + total_point):.1f} more!")
