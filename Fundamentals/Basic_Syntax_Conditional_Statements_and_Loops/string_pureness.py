n = int(input())

for _ in range(0, n):
    word = input()
    is_pure = True

    for index in range(len(word)):
        if word[index] == "," or word[index] == "." or word[index] == "_":
            is_pure = False
            break

    if is_pure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
