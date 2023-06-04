import os


def file_root(file_name):
    path_to_root = os.path.dirname(os.path.abspath(__file__))
    f_root = os.path.join(path_to_root, f"{file_name}")
    return f_root


def create_file(file_name):
    open(file_root(file_name), "w").close()


def add_to_file(file_name, content):
    with open(file_root(file_name), "a") as file:
        file.writelines(content + "\n")


def replace(file_name, old_string, new_string):
    try:
        with open(file_root(file_name), "r+") as file:
            text = file.read()
            text = text.replace(old_string, new_string)
            file.seek(0)
            file.write(text)

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_root(file_name))
    except FileNotFoundError:
        print("An error occurred")


while True:
    command, *data = input().split("-")

    if command == "End":
        break

    if command == "Create":
        create_file(*data)
    elif command == "Add":
        add_to_file(*data)
    elif command == "Replace":
        replace(*data)
    elif command == "Delete":
        delete_file(*data)
