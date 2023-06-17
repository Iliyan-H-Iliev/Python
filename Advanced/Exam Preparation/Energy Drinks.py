from collections import deque

drunk_coffeine = 0

milligrams_coffeine = deque([int(x) for x in input().split(", ")])
energy_drink = deque([int(x) for x in input().split(", ")])

while milligrams_coffeine and energy_drink:

    coffeine = milligrams_coffeine.pop()
    drink = energy_drink.popleft()

    the_drink = coffeine * drink

    if the_drink <= 300 - drunk_coffeine:
        drunk_coffeine += the_drink
    else:
        energy_drink.append(drink)
        drunk_coffeine = max(0, drunk_coffeine - 30)

if energy_drink:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drink)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {drunk_coffeine} mg caffeine.")
