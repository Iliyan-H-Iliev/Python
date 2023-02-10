def no_vowels(some_text):
    vowels = ['a', 'o', 'u', 'e', 'i']
    result = [char for char in some_text if char.lower() not in vowels]
    return "".join(result)


text = input()

print(no_vowels(text))
