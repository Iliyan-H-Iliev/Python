string_input = list(input())
capital_letters_indices = []

for i in range(len(string_input)):
    if string_input[i].isupper():
        capital_letters_indices.append(i)

print(capital_letters_indices)
