from collections import deque

elfs = deque([int(x) for x in input().split()])
boxes = deque([int(x) for x in input().split()])




def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < rows



directions = {
    "up": lambda r, c: [(r - 1) % SIZE, c],
    "down": lambda r, c: [(r + 1) % SIZE, c],
    "left": lambda r, c: [r, (c - 1) % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],

}
