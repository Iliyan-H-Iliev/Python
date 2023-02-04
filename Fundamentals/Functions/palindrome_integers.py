def palindrome_number(n):
    n_list = [n[i] for i in range(len(n))]
    r_list = n_list[::-1]

    if n_list == r_list:
        return True
    else:
        return False


numbers_list = [x for x in input().split(", ")]

for el in numbers_list:
    print(palindrome_number(el))
