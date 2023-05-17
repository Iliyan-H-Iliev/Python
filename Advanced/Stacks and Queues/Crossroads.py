from collections import deque

green_light = int(input())
yellow_light = int(input())

cars = deque()
passed_cars = 0

while True:
    car = input()

    if car == "END":
        break

    if car != "green":
        cars.append(car)
        continue

    if not cars:
        continue

    time_for_moving = green_light + yellow_light

    for _ in range(len(cars)):
        current_car = cars.popleft()

        if len(current_car) <= time_for_moving:
            passed_cars += 1
            time_for_moving -= len(current_car)
        else:
            print("A crash happened!")
            print(f"{current_car} was hit at {current_car[time_for_moving]}.")
            exit()

        if time_for_moving <= yellow_light:
            break

print("Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")
