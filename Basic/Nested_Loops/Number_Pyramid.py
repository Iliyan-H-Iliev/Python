n = int(input())

counter = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        counter += 1

        print(f"{counter}", end=" ") if i != j else print(f"{counter}")

        if n == counter:
            break
    if n == counter:
        break