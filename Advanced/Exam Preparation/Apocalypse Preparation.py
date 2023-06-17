from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament = deque([int(x) for x in input().split()])

healing_item = {
    30: ["Patch", 0],
    40: ["Bandage", 0],
    100: ["MedKit", 0],
}

while textiles and medicament:
    textile = textiles.popleft()
    med = medicament.pop()
    element = textile + med

    if element >= 100:
        healing_item[100][1] += 1
        if medicament:
            medicament.append(medicament.pop() + element - 100)
    elif element != 30 and element != 40:
        medicament.append(med + 10)
    else:
        healing_item[element][1] += 1


if not textiles and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not  medicament:
    print("Medicaments are empty.")

for item, value in sorted(healing_item.values(), key=lambda x: (-x[1], x[0])):
    if value != 0:
        print(f"{item} - {value}")

if medicament:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicament))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
