import re

text = input()

pattern = r"(\*\*|::)([A-Z][a-z]{2,})\1"

digits = [int(ch) for ch in text if ch.isdigit()]
emojis = re.findall(pattern, text)
cool_emojis = []
cool_threshold = 1

for el in digits:
    cool_threshold *= el

for emoji in emojis:
    emoji_threshold = 0
    for ch in emoji[1]:
        emoji_threshold += ord(ch)

    if emoji_threshold >= cool_threshold:
        cool_emojis.append(emoji[0] + emoji[1] + emoji[0])


print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep="\n")
