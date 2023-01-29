number = int(input())

for i in range(1111, 10000):
    for char in str(i):
        if int(char) == 0 or number % int(char) != 0:
            break

    else:
        print(f'{i}', end=" ")
