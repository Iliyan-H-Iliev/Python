from collections import deque

string = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_color = {"orange", "purple", "green"}
secondary_colors_dict = {"orange": {"red", "yellow"},
                         "purple": {"red", "blue"},
                         "green": {"yellow", "blue"}
}
made_colors = []

while string:
    first_string = string.popleft()
    second_string = string.pop() if string else ""

    for color in (first_string + second_string, second_string + first_string):
        if color in colors:
            made_colors.append(color)
            break
    else:
        for el in (first_string[:-1], second_string[:-1]):
            if el:
                string.insert(len(string) // 2, el)

for color in secondary_color.intersection(made_colors):
    if not secondary_colors_dict[color].issubset(made_colors):

        made_colors.remove(color)

print(made_colors)
