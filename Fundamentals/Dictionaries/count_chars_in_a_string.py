text = [x for x in input() if x != " "]

char_count = {}

for char in text:

    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

for key, value in char_count.items():
    print(f"{key} -> {value}")
