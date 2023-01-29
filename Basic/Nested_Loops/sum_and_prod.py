n = int(input())

is_found = False

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):

                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    is_found = True

                elif (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_found = True

                if is_found:
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

if not is_found:
    print("Nothing found")
