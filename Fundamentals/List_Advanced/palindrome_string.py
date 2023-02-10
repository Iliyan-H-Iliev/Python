string_input = input().split()
palindrome = input()

palindrome_list = []

for word in string_input:
    # if word == "".join(reversed(word)):
    if word == word[::-1]:
        palindrome_list.append(word)

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")
