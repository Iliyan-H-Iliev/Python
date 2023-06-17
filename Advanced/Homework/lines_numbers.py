from string import punctuation

first_path = "text.txt"
second_path = "output.txt"

with open(first_path, "r") as text_file, open(second_path, "w") as output_file:
    for row, data in enumerate(text_file):
        count_of_letters = len([x for x in data if x.isalpha()])
        count_of_symbols = len([x for x in data if x in punctuation])

        output_file.write(f"Line {row + 1}: {data.strip()} ({count_of_letters})({count_of_symbols})\n")

