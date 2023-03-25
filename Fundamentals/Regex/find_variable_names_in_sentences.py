import re

pattern = r"(?<=\b[_])[A-Za-z0-9]+\b"

text = input()

result = re.findall(pattern, text)

print(*result, sep=",")
