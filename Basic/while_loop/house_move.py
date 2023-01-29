width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

while total_space > 0:
    boxes = input()

    if boxes != "Done":
        total_space -= int(boxes)
    else:
        break

if total_space >= 0:
    print(f"{total_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
