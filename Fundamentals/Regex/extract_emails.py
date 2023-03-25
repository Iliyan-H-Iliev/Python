import re

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[-._]?[A-Za-z0-9]+@[A-Za-z0-9]+-?[A-Za-z0-9]+\.[A-Za-z]+\.?[A-Za-z]+\b"

text = input()

result = re.finditer(pattern, text)

for el in result:
    print(el[0])
