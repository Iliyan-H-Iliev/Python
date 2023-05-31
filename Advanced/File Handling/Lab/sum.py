import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "numbers.txt")

file = open(file_path, "r")



print(file.read().split("\n"))