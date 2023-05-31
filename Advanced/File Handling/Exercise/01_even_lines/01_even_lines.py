import os
symbols = ["-", ",", ".", "!", "?"]

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "text.txt")

with open(file_path, "r") as file:
    text_lines = file.readlines()

    for i in range(0, len(text_lines), 2):
        new_text = text_lines[i][:-1]
        for symbol in symbols:
            new_text = new_text.replace(symbol, "@")

        print(*new_text.split()[::-1])



