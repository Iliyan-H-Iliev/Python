def even_odd(*args):

    command = args[-1]

    def even():
        return [x for x in args[:-1] if x % 2 == 0]

    def odd():
        return [x for x in args[:-1] if x % 2 != 0]

    if command == "even":
        return even()
    elif command == "odd":
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, "even"))