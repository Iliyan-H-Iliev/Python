def how_long(word):
    return 6 <= len(word) <= 10


def letters_and_digits(word):
    return word.isalnum()


def min_2_digits(word):
    count = 0
    for el in word:
        if el.isdigit():
            count += 1
    return count >= 2


password = input()
is_valid = True

if not how_long(password):
    print("Password must be between 6 and 10 characters")
    is_valid = False
if not letters_and_digits(password):
    print("Password must consist only of letters and digits")
    is_valid = False
if not min_2_digits(password):
    print("Password must have at least 2 digits")
    is_valid = False
if is_valid:
    print("Password is valid")
