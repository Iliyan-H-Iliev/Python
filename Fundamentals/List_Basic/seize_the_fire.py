fires_levels = list(input().split("#"))
water = int(input())
cells = []
total_fire = 0
effort = 0

for el in fires_levels:
    current_elements = el.split(" = ")
    water_needed = int(current_elements[1])

    if water - water_needed < 0:
        continue

    if "High" in current_elements and 81 <= water_needed <= 125:
        cells.append(water_needed)
        total_fire += water_needed
        effort += water_needed * 0.25
        water -= water_needed
    elif "Medium" in current_elements and 51 <= water_needed <= 80:
        cells.append(water_needed)
        total_fire += water_needed
        effort += water_needed * 0.25
        water -= water_needed
    elif "Low" in current_elements and 1 <= water_needed <= 50:
        cells.append(water_needed)
        total_fire += water_needed
        effort += water_needed * 0.25
        water -= water_needed

print("Cells:")
for elem in cells:
    print(f" - {elem}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
