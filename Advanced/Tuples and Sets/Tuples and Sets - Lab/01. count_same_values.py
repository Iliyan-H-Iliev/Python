numbers_data = tuple(float(x) for x in input().split())

numb_counter = {}

for el in numbers_data:
    if el not in numb_counter:
        numb_counter[el] = 0

    numb_counter[el] += 1

for n, c in numb_counter.items():
    print(f"{n} - {c} times")
