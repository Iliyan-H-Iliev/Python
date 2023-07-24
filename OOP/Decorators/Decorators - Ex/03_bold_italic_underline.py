def make_bold(fn):
    def wrapper(*args):
        result = fn(*args)
        return f"<b>{result}</b>"
    return wrapper


def make_italic(fn):
    def wrapper(*args):
        result = fn(*args)
        return f"<i>{result}</i>"
    return wrapper


def make_underline(fn):
    def wrapper(*args):
        result = fn(*args)
        return f"<u>{result}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))