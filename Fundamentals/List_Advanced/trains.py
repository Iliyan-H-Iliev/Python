def add(list_1, p):
    list_1[-1] += p


def insert(list_1, index, p):
    list_1[index] += p


def leave(list_1, index, p):
    list_1[index] -= p


n = int(input())

train = [0] * n

while True:
    commands = input().split()
    command = commands[0]

    if command == "End":
        break

    if command == "add":
        add(train, int(commands[1]))
    elif command == "insert":
        insert(train, int(commands[1]), int(commands[2]))
    elif command == "leave":
        leave(train, int(commands[1]), int(commands[2]))

print(train)
