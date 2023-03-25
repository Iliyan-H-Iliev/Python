text = input()

result_text = []
result_count = []

key = ""
value = ""
result = ""

unique_symbols = ""
unique_count = 0

for i in range(len(text)):
    ch = text[i].upper()

    if i == len(text) - 1:
        result_text.append(key)
        value += ch
        result_count.append(int(value))

    if ch.isdigit() and value:
        value += ch
        continue
    elif not ch.isdigit() and value:
        result_text.append(key)
        result_count.append(int(value))
        key = ""
        value = ""

    if not ch.isdigit():
        key += ch
        if ch not in unique_symbols:
            unique_symbols += ch
            unique_count += 1
    else:
        value += ch

print(f"Unique symbols used: {unique_count}")

for i in range(len(result_text)):
    result += (result_text[i] * result_count[i])

print(result)
