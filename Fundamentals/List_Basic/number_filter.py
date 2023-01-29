n = int(input())
numbers_list = []
filtered = []

for _ in range(n):
    number = int(input())
    numbers_list.append(number)

command = input()

if command == "even":
    for el in numbers_list:
        if el % 2 == 0:
            filtered.append(el)
elif command == "odd":
    for el in numbers_list:
        if el % 2 == 1:
            filtered.append(el)
elif command == "positive":
    for el in numbers_list:
        if el >= 0:
            filtered.append(el)
elif command == "negative":
    for el in numbers_list:
        if el < 0:
            filtered.append(el)

print(filtered)
