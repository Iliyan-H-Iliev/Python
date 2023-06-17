from collections import deque

elfs = deque([int(x) for x in input().split()])
boxes = deque([int(x) for x in input().split()])

count = 0
made_gifts = 0
spend_energy = 0

while len(boxes) > 0 and len(elfs) > 0:

    current_elf = elfs.popleft()

    if current_elf < 5:
        continue

    count += 1

    current_box = boxes.pop()

    if current_elf < current_box:
        current_elf = current_elf * 2
        elfs.append(current_elf)
        boxes.append(current_box)
        continue

    if count % 5 == 0 and count % 3 == 0:
        if current_elf >= current_box * 2:
            current_elf -= ((current_box * 2) - 1)
            spend_energy += current_box * 2
            elfs.append(current_elf)
        else:
            current_elf *= 2
            elfs.append(current_elf)
            boxes.append(current_box)
    elif count % 5 == 0:
        current_elf -= current_box
        spend_energy += current_box
        elfs.append(current_elf)
    elif count % 3 == 0:
        if current_elf >= current_box * 2:
            made_gifts += 2
            spend_energy += current_box * 2
            current_elf -= ((current_box * 2) - 1)
            elfs.append(current_elf)
        else:
            current_elf *= 2
            elfs.append(current_elf)
            boxes.append(current_box)
    elif current_elf >= current_box:
        made_gifts += 1
        spend_energy += current_box
        current_elf -= (current_box - 1)
        elfs.append(current_elf)

print(f"Toys: {made_gifts}")
print(f"Energy: {spend_energy}")
if elfs:
    print(f"Elves left: {', '.join(str(x) for x in elfs)}")
if boxes:
    print(f"Boxes left: {', '.join(str(x) for x in boxes)}")
