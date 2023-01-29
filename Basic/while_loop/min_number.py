from sys import maxsize

min_num = maxsize

while True:
    input_num = input()

    if input_num == "Stop":
        break

    num = int(input_num)

    if num < min_num:
        min_num = num

print(min_num)