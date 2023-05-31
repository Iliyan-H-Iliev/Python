import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "text.txt")

try:
    open(file_path, "r")
    print("File found")
except FileNotFoundError:
    print("file not found")

