text = input()

while True:
    input_com = input()

    if input_com == "Decode":
        break

    command_args = input_com.split("|")
    command = command_args[0]

    if command == "Move":
        number_of_letters = int(command_args[1])
        text = text[number_of_letters:] + text[:number_of_letters]

    elif command == "Insert":
        index = int(command_args[1])
        value = command_args[2]
        text = text[:index] + value + text[index:]

    elif command == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")
