n = int(input())

is_balanced = True
is_opened = False
is_closed = False
is_error = False

for _ in range(n):
    string_input = input()

    if string_input == ")" and not is_opened:
        is_balanced = False
        is_error = True

    elif string_input == "(" and is_balanced:
        is_opened = True
        is_balanced = False

    elif string_input == ")" and is_opened:
        is_closed = True
        is_balanced = True

    elif string_input == "(" and not is_closed:
        is_balanced = False
        is_error = True

if is_balanced and is_opened and is_closed and not is_error:
    print("BALANCED")
else:
    print("UNBALANCED")
