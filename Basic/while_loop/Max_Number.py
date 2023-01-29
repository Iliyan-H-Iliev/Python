from sys import maxsize

max_num = -maxsize

while True:
    input_num = input()

    if input_num == "Stop":
        break

    num = int(input_num)

    if num > max_num:
        max_num = num

print(max_num)
