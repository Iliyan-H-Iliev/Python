list_input = input().split()

counter = 0
is_you_won = False

while True:

    command = input()

    if command == "end":
        break

    counter += 1

    command_list = [int(x) for x in command.split()]
    command_list.sort()
    x1 = command_list[0]
    x2 = command_list[1]

    if x1 < 0 or x2 >= len(list_input) or x1 == x2:
        list_input.insert(int(len(list_input) / 2), f"-{counter}a")
        list_input.insert(int(len(list_input) / 2), f"-{counter}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if list_input[x1] != list_input[x2]:
        print("Try again!")

    if list_input[x1] == list_input[x2]:
        print(f'Congrats! You have found matching elements - {list_input[x1]}!')
        list_input.pop(x2)
        list_input.pop(x1)

    if not list_input:
        is_you_won = True
        break

if is_you_won:
    print(f"You have won in {counter} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(list_input))
