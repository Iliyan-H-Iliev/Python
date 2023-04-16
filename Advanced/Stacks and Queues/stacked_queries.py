n = int(input())

stck = []

for _ in range(n):
    data = input().split()
    command = data[0]

    if command == "1":
        num = int(data[1])
        stck.append(num)
    if stck:
        if command == "2":
            stck.pop()
        elif command == "3":
            print(max(stck))
        elif command == "4":
            print(min(stck))


nnn = len(stck)

for i in range(nnn):
    if i != nnn - 1:
        print(stck.pop(), end=", ")
    else:
        print(stck.pop(), end=" ")
