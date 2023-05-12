longest_intersection = []

for _ in range(int(input())):
    x, y = input().split("-")

    start_1, end_1 = x.split(",")
    start_2, end_2 = y.split(",")

    set_1 = set(x for x in range(int(start_1), int(end_1) + 1))
    set_2 = set(x for x in range(int(start_2), int(end_2) + 1))

    set_3 = set_1.intersection(set_2)

    if len(set_3) > len(longest_intersection):
        longest_intersection = list(set_3)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
