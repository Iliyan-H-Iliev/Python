from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
total_honey = 0

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while bees and nectar:
    bee = bees.popleft()
    collected_nectar = nectar.pop()

    if bee > collected_nectar:
        bees.appendleft(bee)
    elif bee < collected_nectar:
        total_honey += abs(operations[symbols.popleft()](bee, collected_nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: ", end="")
    print(*bees, sep=", ")
if nectar:
    print(f"Nectar left: ", end="")
    print(*nectar, sep=", ")
