while True:
    new_word = ""
    word = input()

    if word == "End":
        break

    if word == "SoftUni":
        continue

    for index in range(len(word)):
        new_word += word[index] + word[index]

    print(new_word)
