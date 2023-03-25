import re

text = input().lower()
word = input().lower()

pattern = re.compile(r'\b' + word + r'\b')

result = re.findall(pattern, text)

print(len(result))
