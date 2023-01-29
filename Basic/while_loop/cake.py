width = int(input())
lenght = int(input())

total_peaces = width * lenght

while total_peaces >= 0:
    peaces = input()

    if peaces != "STOP":
        total_peaces -= int(peaces)
    else:
        break

if total_peaces >= 0:
    print(f"{total_peaces} pieces are left." )
else:
    print(f"No more cake left! You need {abs(total_peaces)} pieces more.")