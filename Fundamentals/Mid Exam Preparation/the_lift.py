waiting_people = int(input())
current_state = [int(x) for x in input().split()]

wagon_capacity = 4

for i in range(len(current_state)):
    space = wagon_capacity - current_state[i]
    people = min(waiting_people, space)
    current_state[i] += people
    waiting_people -= people
    if waiting_people == 0:
        break

if current_state[-1] < wagon_capacity and waiting_people == 0:
    print("The lift has empty spots!")
elif waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(*current_state, sep=" ")
