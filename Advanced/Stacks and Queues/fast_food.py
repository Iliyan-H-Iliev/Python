from collections import deque

food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: ", end="")
    while orders:
        print(orders.popleft(), end=" ")
else:
    print("Orders complete")
