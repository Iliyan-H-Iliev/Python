import re

pattern = r"\d+"

text = input()
while text != "":

    result = re.findall(pattern, text)

    for el in result:
        if el:
            print(el, end=" ")

    text = input()
