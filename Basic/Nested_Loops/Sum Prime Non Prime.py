prime_sum = 0
non_prime_sum = 0

while True:
    command = input()

    if command == "stop":
        break

    num = int(command)
    is_prime = True

    if num < 0:
        print(f"Number is negative.")
        continue

    for number in range(2, num):
        if num % number == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += num
    else:
        non_prime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
