target_list = [int(x) for x in input().split()]


while True:
    command = input()

    if command == "End":
        break

    index = int(command)
    # index check
    if index >= len(target_list):
        continue

    index_val = target_list[index]
    target_list[index] = -1

    for i in range(len(target_list)):
        if target_list[i] == -1:
            continue
        if target_list[i] > index_val:
            target_list[i] -= index_val
        else:
            target_list[i] += index_val

target_list_as_str = [str(x) for x in target_list]

print(f"Shot targets: {target_list.count(-1)} -> {' '.join(target_list_as_str)}")
