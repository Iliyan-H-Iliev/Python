from collections import deque

queues = deque()

while True:
    person = input()

    if person == "End":
        print(f"{len(queues)} people remaining.")
        break

    if person == "Paid":
        print("\n".join(queues))
        queues.clear()
    else:
        queues.append(person)
