import re

text = input()
find_words = []

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

words = re.findall(pattern, text)

if words:
    print(f"{len(words)} word pairs found!")
else:
    print("No word pairs found!")

for word in words:
    if word[1][::-1] == word[2]:
        find_words.append(word[1] + " <=> " + word[2])

if find_words:
    print("The mirror words are:")
    print(*find_words, sep=", ")
else:
    print("No mirror words!")
