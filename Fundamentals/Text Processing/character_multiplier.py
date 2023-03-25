text_input = input().split()

word_1 = ""
word_2 = ""
dif = ""
result = 0

if len(text_input[0]) >= len(text_input[1]):
    word_1 = text_input[0]
    word_2 = text_input[1]
    dif = word_1[len(word_2):]
    word_1 = word_1[:len(word_2)]

else:
    word_1 = text_input[1]
    word_2 = text_input[0]
    dif = word_1[len(word_2):]
    word_1 = word_1[:len(word_2)]

for i in range(len(word_1)):
    result += ord(word_1[i]) * ord(word_2[i])

if dif:
    for el in dif:
        result += ord(el)

print(result)
