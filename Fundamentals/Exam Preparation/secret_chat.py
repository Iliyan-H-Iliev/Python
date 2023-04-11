message = input()

while True:
    data = input()

    if data == "Reveal":
        break

    command_args = data.split(":|:")
    command = command_args[0]

    if command == "InsertSpace":
        index = int(command_args[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif command == "Reverse":
        substring = command_args[1]

        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")

    elif command == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]

        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")
