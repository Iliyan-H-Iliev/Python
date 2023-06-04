import os


def extension_filling(file_in_dir):
    file_extension, *file_name = file_in_dir.split(".")[::-1]
    if file_extension not in extensions:
        extensions[file_extension] = []
    extensions[file_extension].append(f"{'.'.join(x for x in file_name[::-1])}")


extensions = {}

path_to_root = input("Please enter a directory: ")
while True:
    if not os.path.isdir(path_to_root):
        path_to_root = input("Please enter a correct directory: ")
    else:
        break

for zero_level_file in os.listdir(path_to_root):
    if os.path.isdir(os.path.join(path_to_root, zero_level_file)):
        for first_level_file in os.listdir(os.path.join(path_to_root, zero_level_file)):
            if not os.path.isdir(os.path.join(path_to_root, zero_level_file, first_level_file)):
                extension_filling(first_level_file)
    else:
        extension_filling(zero_level_file)

file_root = os.path.join(path_to_root, "report.txt")

with open(file_root, "w") as file:
    for extension, names in sorted(extensions.items(), key=lambda x: (x[0], x[1])):
        file.write(f".{extension}\n")
        for name in names:
            file.write(f"- - - {name}.{extension}\n")
