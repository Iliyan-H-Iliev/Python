def sorting_cheeses(**kwargs):
    result = ""
    for k, v in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{k}\n"
        for el in sorted(v)[::-1]:
            result += f"{el}\n"
    return result


print(
    sorting_cheeses(
            Parmesan=[102, 120, 135],
            Camembert=[100, 100, 105, 500, 430],
            Mozzarella=[50, 125],
                    )
    )