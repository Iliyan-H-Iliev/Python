num = int(input())
number = 1
for i in range(0, num + 1, 2):
    if i == 0:
        print(number)
    else:
        number *= 2 * 2
        print(number)
