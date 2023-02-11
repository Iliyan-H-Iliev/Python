def divide_word(word, parts):
    result = []
    # word_list = [x for x in word]
    partition_size = len(word) // parts
    # current_word = ""
    position = 0
    for i in range(parts - 1):
        result.append(word[position:position + partition_size])
        position += partition_size
    result.append(word[position:])
    return result


print(divide_word("abcde1", 3))
