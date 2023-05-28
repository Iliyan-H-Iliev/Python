def grocery_store(**kwargs):
    res = ""

    for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        res += f"{k}: {v}\n"

    return res


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
