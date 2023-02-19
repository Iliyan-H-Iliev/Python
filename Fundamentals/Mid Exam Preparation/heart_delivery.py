neighborhood = [int(x) for x in input().split("@")]
house_number = 0

while True:

    command = input()

    if command == "Love!":
        break

    command_arg = command.split()
    index = command_arg[1]

    house_number += int(index)

    if house_number >= len(neighborhood):
        house_number = 0

    if neighborhood[house_number] == 0:
        print(f"Place {house_number} already had Valentine's day.")
        continue

    neighborhood[house_number] -= 2

    if neighborhood[house_number] == 0:
        print(f"Place {house_number} has Valentine's day.")

valentines_day_houses = neighborhood.count(0)


print(f"Cupid's last position was {house_number}.")

if valentines_day_houses == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - valentines_day_houses} places.")
