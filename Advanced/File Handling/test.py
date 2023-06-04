import os


def file_root(file_name):
    path_to_root = os.path.dirname(os.path.abspath(__file__))
    f_root = os.path.join(path_to_root, f"{file_name}")
    return f_root


def replace(file_name, old_string, new_string):
    try:
        with open(file_root(file_name), "r+") as file:
            text = file.read()
            text = text.replace(old_string, new_string)
            print(text)
            file.seek(0, 0)
            file.write(text)

    except FileNotFoundError:
        print("An error occurred")


replace("text.txt", "asdf", "asdfggggggg")