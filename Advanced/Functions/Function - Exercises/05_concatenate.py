def concatenate(*args, **kwargs):
    result = ""

    for el in args:
        result += el

    for k, v in kwargs.items():
        result = result.replace(k, v)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!",
                  UNI="Uni", Grate="Great"))
