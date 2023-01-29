count_group = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

total_people = 0

for i in range(1, count_group + 1):
    group = int(input())

    if group <= 5:
        musala += group
    elif group <= 12:
        monblan += group
    elif group <= 25:
        kilimandjaro += group
    elif group <= 40:
        k2 += group
    else:
        everest += group

    total_people += group

print(f'{(musala/total_people) * 100:.2f}%')
print(f'{(monblan/total_people) * 100:.2f}%')
print(f'{(kilimandjaro/total_people) * 100:.2f}%')
print(f'{(k2/total_people) * 100:.2f}%')
print(f'{(everest/total_people) * 100:.2f}%')
