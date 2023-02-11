rooms_numbers = int(input())

total_free_chairs = 0
is_enough_chairs = True

for i in range(1, rooms_numbers + 1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])

    if visitors < chairs:
        total_free_chairs += chairs - visitors

    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        is_enough_chairs = False

if is_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
