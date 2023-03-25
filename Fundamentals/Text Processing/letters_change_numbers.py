from string import ascii_lowercase, ascii_uppercase

text = input().split()

uppercase = [x for x in ascii_uppercase]
lowercase = [x for x in ascii_lowercase]

total_sum = 0


for el in text:

    first_operation = el[0]
    second_operation = el[-1]
    number = int(el[1:-1])

    if first_operation.isupper():
        number /= (uppercase.index(first_operation) + 1)
    else:
        number *= (lowercase.index(first_operation) + 1)

    if second_operation.isupper():
        number -= (uppercase.index(second_operation) + 1)
    else:
        number += (lowercase.index(second_operation) + 1)

    total_sum += number

print(f"{total_sum:.2f}")
