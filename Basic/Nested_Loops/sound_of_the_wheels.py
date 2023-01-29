m = int(input())

count = 0
is_password = False
pwd = 0

for a in range(1, 9 + 1):

    for b in range(1, 9 + 1):

        for c in range(1, 9 + 1):

            for d in range(1, 9 + 1):

                if a < b and c > d:
                    if a * b + c * d == m:
                        count += 1
                        if count == 4:
                            is_password = True
                            pwd = f'{a}{b}{c}{d}'
                        print(f'{a}{b}{c}{d}', end=' ')

print("")

if is_password:
    print(f'Password: {pwd}')
else:
    print('No!')
