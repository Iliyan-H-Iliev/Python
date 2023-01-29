n = int(input())
capacity = 0 #255

for _ in range(n):
    liters_water = int(input())

    if capacity + liters_water <= 255:
        capacity += liters_water
    else:
        print("Insufficient capacity!")
        continue
print(capacity)
