key = int(input())
n = int(input())

messages = ""

for _ in range(n):
    letter = input()
    messages += chr(ord(letter) + key)

print(messages)
