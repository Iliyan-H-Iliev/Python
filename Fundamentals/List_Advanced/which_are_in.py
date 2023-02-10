which_are_in = input().split(", ")
string_list = input().split(", ")

are_in = []

for el in which_are_in:
    for elem in string_list:
        if el in elem:
            are_in.append(el)
            break

print(are_in)
