password = input()

while True:
    comm = input()

    if comm == "Done":
        break

    command_args = comm.split()
    command = command_args[0]

    if command == "TakeOdd":
        odd_index_password = ""

        for i in range(len(password)):
            if i % 2 != 0:
                odd_index_password += password[i]

        password = odd_index_password
        print(password)

    elif command == "Cut":
        index = int(command_args[1])
        length = int(command_args[2])

        password = password[:index] + password[index + length:]
        print(password)

    elif command == "Substitute":
        substring = command_args[1]
        substitute = command_args[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
