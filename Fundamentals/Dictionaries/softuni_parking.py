n = int(input())
parking_register = {}

for _ in range(n):
    command = input().split()
    name = command[1]

    if command[0] == "register":
        number_plate = command[2]
        if name in parking_register:
            print(f"ERROR: already registered with plate number {parking_register[name]}")
        else:
            parking_register[name] = number_plate
            print(f"{name} registered {number_plate} successfully")
    else:
        if name in parking_register:
            parking_register.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for username, numb in parking_register.items():
    print(f"{username} => {numb}")
