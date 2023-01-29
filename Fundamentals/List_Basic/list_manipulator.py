from sys import maxsize
number_list = [int(s) for s in input().split()]

while True:
    command = list(input().split())

    if command[0] == "end":
        break

    if "exchange" in command:
        if int(command[1]) >= len(number_list) or int(command[1]) < 0:
            print("Invalid index")
        else:
            number_list = number_list[int(command[1]) + 1:] + number_list[:int(command[1]) + 1]

    elif "max" in command:
        numb = -maxsize
        index = None
        if command[1] == "even":
            for i in range(len(number_list)):
                if number_list[i] % 2 == 0 and number_list[i] >= numb:
                    index = i
                    numb = number_list[i]
        elif command[1] == "odd":
            for i in range(len(number_list)):
                if number_list[i] % 2 == 1 and number_list[i] >= numb:
                    index = i
                    numb = number_list[i]
        if index or index == 0:
            print(index)
        else:
            print("No matches")

    elif "min" in command:
        numb = maxsize
        index = None
        if command[1] == "even":
            for i in range(len(number_list)):
                if number_list[i] % 2 == 0 and number_list[i] <= numb:
                    index = i
                    numb = number_list[i]
        elif command[1] == "odd":
            for i in range(len(number_list)):
                if number_list[i] % 2 == 1 and number_list[i] <= numb:
                    index = i
                    numb = number_list[i]
        if index or index == 0:
            print(index)
        else:
            print("No matches")

    elif "first" in command:
        count = int(command[1])
        empty_list = []

        if count > len(number_list):
            print("Invalid count")
            continue

        if command[2] == "even":
            for i in range(len(number_list)):
                if number_list[i] % 2 == 0:
                    empty_list.append(number_list[i])
                if len(empty_list) == count:
                    break
        elif command[2] == "odd":
            for i in range(len(number_list)):
                if number_list[i] % 2 == 1:
                    empty_list.append(number_list[i])
                if len(empty_list) == count:
                    break

        if empty_list:
            print(empty_list)
        else:
            print("[]")

    elif "last" in command:
        count = int(command[1])
        empty_list = []
        if count > len(number_list):
            print("Invalid count")
            continue

        if command[2] == "even":
            for i in range(-1, -len(number_list) - 1, -1):
                if number_list[i] % 2 == 0:
                    empty_list.append(number_list[i])
                if len(empty_list) == count:
                    break
        elif command[2] == "odd":
            for i in range(-1, -len(number_list) - 1, -1):
                if number_list[i] % 2 == 1:
                    empty_list.append(number_list[i])
                if len(empty_list) == count:
                    break

        if empty_list:
            empty_list.reverse()
            print(empty_list)
        else:
            print("[]")
print(number_list)
