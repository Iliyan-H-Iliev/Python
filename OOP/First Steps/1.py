a = {1: 2, 3: 4, 5: 6}
asd = []

for k, v in a.items():
    asd .append(f"{k}: {v}")

print(*asd,sep=", ")