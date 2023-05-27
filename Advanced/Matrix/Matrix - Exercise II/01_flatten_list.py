data = input().split("|")
sub_string = []

for el in data[::-1]:
    sub_string.extend(el.split())

print(*sub_string)