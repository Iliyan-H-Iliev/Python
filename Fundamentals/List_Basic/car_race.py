input_list = list(input().split())

left_car_time = 0
right_car_time = 0

for i in range(int(len(input_list) / 2)):
    if int(input_list[i]) == 0:
        left_car_time *= 0.8
    else:
        left_car_time += int(input_list[i])

for i in range(-1, int(((len(input_list) / 2) + 1) * -1), -1):
    if int(input_list[i]) == 0:
        right_car_time *= 0.8
    else:
        right_car_time += int(input_list[i])

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
