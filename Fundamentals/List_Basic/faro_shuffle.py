cards = list(input().split())
faro_shuffle = int(input())
d = int(len(cards) / 2)
new_list = cards

for _ in range(faro_shuffle):
    first_half = new_list[:d]
    second_half = new_list[d:]
    new_list.clear()
    for i in range(len(first_half)):
        new_list.append(first_half[i])
        new_list.append(second_half[i])

print(new_list)
