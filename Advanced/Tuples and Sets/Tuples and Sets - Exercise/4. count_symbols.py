text = tuple(input())
unique_symbols = set(text)

for el in sorted(unique_symbols):
    print(f"{el}: {text.count(el)} time/s")
