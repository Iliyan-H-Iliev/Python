import string

user_names = input().split(", ")

match = string.ascii_letters + string.digits + "_" + "-"

for el in user_names:
    is_correct = True

    if not 3 < len(el) < 16:
        is_correct = False
        continue

    if not all([x in match for x in el]):
        is_correct = False
        continue

    if is_correct:
        print(el)
