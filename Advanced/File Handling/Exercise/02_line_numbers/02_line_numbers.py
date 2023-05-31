import os
from string import punctuation

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_root = os.path.join(path_to_root, "text.txt")
new_file_root = os.path.join(path_to_root, "output.txt")

with open(file_root, "r") as file:
    file_lines = file.readlines()

with open(new_file_root, "w") as new_file:

    for i in range(len(file_lines)):
        letters = 0
        punctuation_marks = 0
        for symbol in file_lines[i]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                punctuation_marks += 1

        new_file.write(f"Line {i + 1}: {file_lines[i][:-1]} ({letters})({punctuation_marks})\n")
