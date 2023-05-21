first_sequences = set(int(x) for x in input().split())
second_sequences = set(int(x) for x in input().split())

for _ in range(int(input())):
    command_1, command_2, *data = input().split()

    command = command_1 + " " + command_2

    if command == "Add First":
        [first_sequences.add(int(x)) for x in data]
    elif command == "Add Second":
        [second_sequences.add(int(x)) for x in data]
    elif command == "Remove First":
        [first_sequences.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second_sequences.discard(int(x)) for x in data]
    else:
        print(first_sequences > second_sequences or second_sequences > first_sequences)

print(*sorted(first_sequences), sep=", ")
print(*sorted(second_sequences), sep=", ")
