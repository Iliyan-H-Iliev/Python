from collections import deque

string = deque(input().split())
numbs = deque()

while string:
    command = string.popleft()

    if command not in "/*-+":
        numbs.append(int(command))
        continue

    if command == "*":
        for _ in range(len(numbs) - 1):
            numbs.appendleft(numbs.popleft() * numbs.popleft())
    elif command == "/":
        for _ in range(len(numbs) - 1):
            numbs.appendleft(numbs.popleft() // numbs.popleft())
    elif command == "+":
        for _ in range(len(numbs) - 1):
            numbs.appendleft(numbs.popleft() + numbs.popleft())
    elif command == "-":
        for _ in range(len(numbs) - 1):
            numbs.appendleft(numbs.popleft() - numbs.popleft())

print(*numbs)
