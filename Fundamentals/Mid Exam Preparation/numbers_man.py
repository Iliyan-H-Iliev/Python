list_input = [int(x) for x in input().split()]

average_number = (min(list_input) + max(list_input)) / 2

greater_than_an = [x for x in list_input if x > average_number]

greater_than_an.sort(reverse=True)


if not greater_than_an:
    print("No")
elif len(greater_than_an) > 5:
    top_5 = greater_than_an[:5]
    print(*top_5, sep=" ")
else:
    print(*greater_than_an, sep=" ")
