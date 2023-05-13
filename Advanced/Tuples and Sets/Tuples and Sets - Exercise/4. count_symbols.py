text = tuple(input())

for el in sorted(set(text)):
    print(f"{el}: {text.count(el)} time/s")
