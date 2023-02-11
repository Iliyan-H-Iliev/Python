word_list = input().split()

even_word_list = [x for x in word_list if len(x) % 2 == 0]

print(*even_word_list)
