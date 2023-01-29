num = int(input())

max_numb = int(input())
min_numb = max_numb

for _ in range(0, num-1):
    number = int(input())

    if number >= max_numb:
        max_numb = number

    if number <= min_numb:
        min_numb = number

print(f'Max number: {max_numb}')
print(f'Min number: {min_numb}')