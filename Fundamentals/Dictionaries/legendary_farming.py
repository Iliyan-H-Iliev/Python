wanted_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

farming_items = {"shards": 0, "fragments": 0, "motes": 0}

found = False

while not found:
    items = input().lower().split()

    for i in range(1, len(items), 2):
        key = items[i]
        value = int(items[i - 1])

        if key not in farming_items:
            farming_items[key] = value
        else:
            farming_items[key] += value
        if key == "shards" or key == "fragments" or key == "motes":
            if farming_items[key] >= 250:
                farming_items[key] -= 250
                found = True
                print(f"{wanted_items[key]} obtained!")
                break
        if found:
            break

for material, quantity in farming_items.items():
    print(f"{material}: {quantity}")
