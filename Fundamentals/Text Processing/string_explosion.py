text = input().split(">")

strength = 0

for i in range(1, len(text)):
    explosion = int(text[i][0])

    if len(text[i]) >= explosion + strength:
        text[i] = text[i][explosion + strength:]
        strength = 0
    else:
        strength += explosion - len(text[i])
        text[i] = ""

print(*text, sep=">")
