input_string = input()
lower_string = input_string.lower()
counter = 0

beach_list = ["sand", "water", "fish", "sun"]

for word in beach_list:
    if word in lower_string:
        word_count = lower_string.count(word)
        counter += word_count

print(counter)
