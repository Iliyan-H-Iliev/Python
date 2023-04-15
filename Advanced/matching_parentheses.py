data = input()
opened = []

for i in range(len(data)):
    ch = data[i]

    if ch == "(":
        opened.append(i)

    elif ch == ")":
        start = opened.pop()
        print(data[start:i + 1])
