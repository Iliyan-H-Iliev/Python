def characters_loop(s, e):
    result = []
    for i in range(ord(s) + 1, ord(e)):
        result.append(chr(i))
    return result


first_char = input()
second_char = input()

print(" ".join(characters_loop(first_char, second_char)))
