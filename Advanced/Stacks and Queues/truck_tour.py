from collections import deque
number_of_petrol_station = int(input())

petrol_from_pump = deque()
distance = deque()

pump_count = 0
is_found = False

for _ in range(number_of_petrol_station):
    p, d = input().split()
    petrol_from_pump.append(int(p))
    distance.append(int(d))

for i in range(number_of_petrol_station):
    copy_petrol_from_pump = petrol_from_pump.copy()
    copy_distance = distance.copy()
    current_petrol = 0

    for _ in range(number_of_petrol_station):
        petrol = copy_petrol_from_pump.popleft()
        distance_to_next_pump = copy_distance.popleft()

        if current_petrol + petrol >= distance_to_next_pump:
            current_petrol += petrol - distance_to_next_pump
        else:
            break

    if copy_petrol_from_pump:
        petrol_from_pump.rotate(-1)
        distance.rotate(-1)
    else:
        pump_count = i
        break
print(pump_count)
