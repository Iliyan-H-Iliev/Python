activation_key = input()

while True:
    command_input = input()

    if command_input == "Generate":
        break

    command_args = command_input.split(">>>")
    command = command_args[0]

    if command == "Contains":
        substring = command_args[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        case = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        flip_case = ""

        if case == "Upper":
            flip_case = activation_key[start_index:end_index].upper()

        else:
            flip_case = activation_key[start_index:end_index].lower()

        activation_key = activation_key[:start_index] + flip_case + activation_key[end_index:]
        print(activation_key)

    elif command == "Slice":
        start_index = int(command_args[1])
        end_index = int(command_args[2])

        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")