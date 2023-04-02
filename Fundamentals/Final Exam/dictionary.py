words_and_def = input().split(" | ")
test_words = input().split(" | ")
command = input()

dictionary = {}

for el in words_and_def:
    key, value = el.split(": ")

    if key not in dictionary:
        dictionary[key] = []

    dictionary[key].append(value)

if command == "Test":

    for el in test_words:
        if el in dictionary:
            print(f"{el}:")
            for definition in dictionary[el]:
                print(f" -{definition}")

elif command == "Hand Over":

    for k in dictionary.keys():
        print(f"{k}", end=" ")
