path = input().split("\\")

arg = path[-1].split(".")

file_name = arg[0]
extension = arg[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
