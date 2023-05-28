def valid_index(r, c):
    return 0 <= r < n and 0 <= c < n


def knight_check(r, c):
    counter = 0
    for v in movies.values():
        if valid_index(r + v[0], c + v[1]):
            if board[r + v[0]][c + v[1]] == "K":
                counter += 1

    return counter


n = int(input())

board = [list(input()) for _ in range(n)]

removed_knight = 0
attacked_knight = 0
knight_for_removing = []

movies = {
    "lu": (-1, -2),
    "ld": (1, -2),
    "ru": (-1, 2),
    "rd": (1, 2),
    "ul": (-2, -1),
    "ur": (-2, 1),
    "dl": (2, -1),
    "dr": (2, 1),
}

while True:

    for row in range(n):
        for col in range(n):

            if board[row][col] == "0":
                continue

            if knight_check(row, col) > attacked_knight:
                knight_for_removing = [row, col]
                attacked_knight = knight_check(row, col)

    if knight_for_removing:
        board[knight_for_removing[0]][knight_for_removing[1]] = "0"
        removed_knight += 1
        knight_for_removing = []
        attacked_knight = 0
    else:
        break

print(removed_knight)
