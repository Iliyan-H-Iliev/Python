start_num = int(input())
end_num = int(input())
magic_num = int(input())

is_found = False
counter = 0

for num_1 in range(start_num, end_num + 1):

    for num_2 in range(start_num, end_num + 1):
        counter += 1

        if num_1 + num_2 == magic_num:
            is_found = True
            print(f"Combination N:{counter} ({num_1} + {num_2} = {magic_num})")
            break

    if is_found:
        break

else:
    print(f"{counter} combinations - neither equals {magic_num}")
