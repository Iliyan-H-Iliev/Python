from itertools import permutations


def possible_permutations(a_list):
    for el in permutations(a_list):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]