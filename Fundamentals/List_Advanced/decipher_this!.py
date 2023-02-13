secret_message = input().split()
message = []

for i in range(len(secret_message)):
    first_later_in_number = ""
    word = ""
    counter_digit = 0

    for ch in secret_message[i]:

        if ch.isdigit():
            first_later_in_number += ch
            counter_digit += 1

    secret_word = secret_message[i]
    first_later = chr(int(first_later_in_number))

    word = first_later + secret_word[counter_digit:]

    word_reconstruction = [char for char in word]
    word_reconstruction[1], word_reconstruction[-1] = word_reconstruction[-1], word_reconstruction[1]
    message.append("".join(word_reconstruction))

print(*message)
