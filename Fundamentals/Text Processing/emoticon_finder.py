text = input()

for i in range(len(text)):
    result = ""

    if text[i] == ":":
        result = text[i] + text[i + 1]
        i += 2
        print(result)
