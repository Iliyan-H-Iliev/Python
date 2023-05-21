from collections import deque

material = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {
    150: ["Doll", 0],
    250: ["Wooden train", 0],
    300: ["Teddy bear", 0],
    400: ["Bicycle", 0],
}

made_presents = set()
set_1 = {"Teddy bear", "Bicycle"}
set_2 = {"Doll", "Wooden train"}

while material and magic:
    curr_material = material.pop()
    curr_magic = magic.popleft()

    if curr_material * curr_magic < 0:
        material.append(curr_material + curr_magic)
        continue

    if curr_material * curr_magic == 0:
        if curr_material > 0:
            material.append(curr_material)
        elif curr_magic > 0:
            magic.appendleft(curr_magic)
        continue

    if curr_material * curr_magic in presents:
        presents[curr_material * curr_magic][1] += 1
        made_presents.add(presents[curr_material * curr_magic][0])
    else:
        material.append(curr_material + 15)

if set_1.issubset(made_presents) or set_2.issubset(made_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material:
    print(f"Materials left: ", end="")
    print(*reversed(material), sep=", ")
if magic:
    print(f"Magic left: ", end="")
    print(*magic, sep=", ")

for value in sorted(presents.values()):
    if value[1] > 0:
        print(f"{value[0]}: {value[1]}")
