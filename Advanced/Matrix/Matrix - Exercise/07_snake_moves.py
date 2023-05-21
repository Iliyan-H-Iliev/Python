from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

text = deque()

while len(text) <= rows * cols:
    text.extend(word)

for i in range(rows):
    substring = [text.popleft() for _ in range(cols)]
    if i % 2 == 0:
        print(*substring, sep="")
    else:
        print(*substring[::-1], sep="")
