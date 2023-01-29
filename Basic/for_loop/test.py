text = input()

string = len(text)

total = 0
for i in range(0, string):
    current = text[i]

    if current == 'a':
        total += 1
    elif