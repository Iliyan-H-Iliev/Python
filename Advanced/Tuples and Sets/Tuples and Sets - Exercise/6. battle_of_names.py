odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    result = 0

    for el in list(input()):
        result += ord(el)

    result = int(result / i)

    even_set.add(int(result)) if result % 2 == 0 else odd_set.add(int(result))

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_odd_set == sum_even_set:
    print(*(odd_set | even_set), sep=", ")
elif sum_odd_set > sum_even_set:
    print(*(odd_set - even_set), sep=", ")
else:
    print(*(odd_set ^ even_set), sep=", ")
