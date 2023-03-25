import re

pattern = r"www\.[A-Za-z0-9\-]+[A-Za-z0-9]\.[a-z\.]+[a-z]"

text_list = []

while True:
    text = input()

    if text == "":
        break

    text_list.append(text)

for el in text_list:
    link = re.findall(pattern, el)
    if link:
        print(*link)
