from collections import deque

robots_list = input().split(";")
input_time = input().split(":")
robots = {}
elements = deque()
robots_deque = deque()
for el in robots_list:
    key, value = el.split("-")
    robots_deque.append(key)
    robots[key] = int(value)

time = {"Hour": int(input_time[0]), "Min": int(input_time[1]), "Sec": int(input_time[2])}

print(robots_deque)
while True:
    data = input()

    if data == "End":
        break

