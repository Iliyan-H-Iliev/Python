input_list = list(input().split())
n = int(input())

killed = []
index = 0

while input_list:
    index = (index + n - 1) % len(input_list)
    killed.append(input_list.pop(index))

print("[" + ",".join(killed) + "]")
