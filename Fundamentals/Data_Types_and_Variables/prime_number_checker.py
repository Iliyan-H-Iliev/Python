number = int(input())

is_prime = True

for i in range(1, number + 1):
    if i == 1:
        continue
    if number % i == 0 and i != number:
        is_prime = False
        break

if is_prime:
    print("True")
else:
    print("False")
