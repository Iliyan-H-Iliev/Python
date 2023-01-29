n = int(input())
word = input()

all_frases = []
after_search = []

for _ in range(n):
    frase = input()
    all_frases.append(frase)

    if word in frase:
        after_search.append(frase)

print(all_frases)
print(after_search)

