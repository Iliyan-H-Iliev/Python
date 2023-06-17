def naughty_or_nice_list(array, *args, **kwargs):
    result = ""

    kids_list = {
        "Nice": [],
        "Naughty": [],
        "Not found": [],
    }

    kids = []
    for el in array:
        kids.extend(list(el))

    for el in args:
        numb, char = el.split("-")
        numb = int(numb)
        if kids.count(numb) == 1:
            for num, name in array:
                if numb == num:
                    kids_list[char].append(name)
                    array.remove((num, name))
                    kids.remove(name)
                    break

    for name, char in kwargs.items():
        if kids.count(name) == 1:
            kids_list[char].append(name)
            for el in array:
                if el[1] == name:
                    array.remove(el)

    for el in array:
        kids_list["Not found"].append(el[1])

    for char, names in kids_list.items():
        if names:
            result += f"{char}: {', '.join(x for x in names)}\n"

    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))



print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
