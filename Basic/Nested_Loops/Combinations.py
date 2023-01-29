num = int(input())

counter = 0

for num_1 in range(num + 1):
    for num_2 in range(num + 1):
        for num_3 in range(num + 1):

            if num_1 + num_2 + num_3 == num:
                counter += 1

print(counter)
