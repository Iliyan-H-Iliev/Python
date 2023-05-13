longest_intersection = []

for _ in range(int(input())):
    first_data, second_data = (el.split(",") for el in input().split("-"))

    start_1, end_1 = first_data
    start_2, end_2 = second_data

    set_1 = set(x for x in range(int(start_1), int(end_1) + 1))
    set_2 = set(x for x in range(int(start_2), int(end_2) + 1))

    intersection = set_1.intersection(set_2)

    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is\
{longest_intersection} with length\
{len(longest_intersection)}")
