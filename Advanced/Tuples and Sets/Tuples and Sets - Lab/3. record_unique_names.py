unique_names = set()

for _ in range(int(input())):
    unique_names.add(input())

print(*unique_names, sep="\n")
