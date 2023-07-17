from math import sqrt


def get_primes(a_list):
    for el in a_list:
        if el <= 1:
            continue

        for i in range(2, int(sqrt(el)) + 1):
            if el <= 2 or el % i == 0:
                break
        else:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))