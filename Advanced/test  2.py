from collections import deque

bullet_price = int(input())
gun_barrel_max_size = int(input())

bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])

reward = int(input())

bullets_fired = 0
gun_barrel_size = min(len(bullets), gun_barrel_max_size)

while bullets and locks:

    while gun_barrel_size != 0:
        if locks:
            current_bullet = bullets.pop()
            current_lock = locks.popleft()
            bullets_fired += 1
            gun_barrel_size -= 1
        else:
            break

        if current_bullet > current_lock:
            locks.appendleft(current_lock)
            print("Ping!")
        else:
            print("Bang!")

    if bullets and gun_barrel_size == 0:
        if len(bullets) <= gun_barrel_max_size:
            gun_barrel_size = len(bullets)
        else:
            gun_barrel_size = gun_barrel_max_size
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${abs(reward - bullets_fired * bullet_price)}")
