import os


while True:
    command, *info = input().split("-")

    if command == "End":
        break

    file_path = info[0]

    if command == "Create":
        with open(file_path, "w"):
            pass

    elif command == "Add":
        with open(file_path, "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(file_path, "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"An error occurred")


