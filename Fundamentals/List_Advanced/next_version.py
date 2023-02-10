current_version = [int(x) for x in input().split(".")]
current_version[-1] += 1

for i in range(len(current_version) - 1, 0, -1):
    if current_version[i] > 9:
        current_version[i] = 0
        current_version[i - 1] += 1

print(".".join(str(x) for x in current_version))
