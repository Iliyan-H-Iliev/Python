from collections import deque

water_in_dispenser = int(input())
people_q = deque()

while True:
    data = input()
    if data == "Start":
        break
    people_q.append(data)

while True:
    command = input()
    if command == "End":
        break

    if command.isdigit():
        person = people_q.popleft()
        liters = int(command)
        if liters <= water_in_dispenser:
            print(f"{person} got water")
            water_in_dispenser -= liters
        else:
            print(f"{person} must wait")
    else:
        comm = command.split()
        liters = int(comm[1])
        water_in_dispenser += liters

print(f"{water_in_dispenser} liters left")
