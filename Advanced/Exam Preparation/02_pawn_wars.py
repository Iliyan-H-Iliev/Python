def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < rows


def capture(r, c):
    diagonals = {
        "ul": (-1, -1),
        "ur": (-1, 1),
        "dl": (1, -1),
        "dr": (1, 1)
    }
    for i_1, i_2 in diagonals.values():
        if valid_index(r + i_1, c + i_2):
            if chessboard[r + i_1][c + i_2] == b or chessboard[r + i_1][c + i_2] == w:
                return [r + i_1, c + i_2]
    return [r, c]


def change_symbol(old_r, old_c, new_r, new_c, s):
    chessboard[old_r][old_c] = "-"
    chessboard[new_r][new_c] = s


def new_position(r, c, s):
    if s == w:
        return [r + 1, c]
    elif s == b:
        return [r - 1, c]


rows = 8

matrix = [[x for x in input().split()] for _ in range(rows)]
chessboard = []
white_pawn_position = []
black_pawn_position = []
winner_coordinate = []
is_queen = False
winner = ""
w, b = "w", "b"

for i in range(rows):
    chessboard.append(matrix.pop())
    if w in chessboard[i]:
        white_pawn_position = [i, chessboard[i].index(w)]
    if b in chessboard[i]:
        black_pawn_position = [i, chessboard[i].index(b)]

while True:

    capture_location = capture(*white_pawn_position)
    new_white_position = new_position(*white_pawn_position, w)

    if capture_location != white_pawn_position or new_white_position[0] == 7:
        change_symbol(*white_pawn_position, *capture_location, w)
        white_pawn_position = [*capture_location] if new_white_position[0] != 7 else [*new_white_position]
        winner = "White"
        is_queen = True if new_white_position[0] == 7 else False
        break

    change_symbol(*white_pawn_position, *new_white_position, w)
    white_pawn_position = [*new_white_position]

    capture_location = capture(*black_pawn_position)
    new_black_position = new_position(*black_pawn_position, b)

    if capture_location != black_pawn_position or new_black_position[0] == 0:
        change_symbol(*black_pawn_position, *capture_location, b)
        black_pawn_position = [*capture_location] if new_black_position[0] != 0 else [*new_black_position]
        winner = "Black"
        is_queen = True if new_black_position[0] == 0 else False
        break

    change_symbol(*black_pawn_position, *new_black_position, b)
    black_pawn_position = [*new_black_position]

if winner == "White":
    winner_coordinate = white_pawn_position
else:
    winner_coordinate = black_pawn_position

if is_queen:
    print(f"Game over! {winner} pawn is promoted to a queen at \
{chr(ord('a') + winner_coordinate[1])}{winner_coordinate[0] + 1}.")
else:
    print(f"Game over! {winner} win, capture on \
{chr(ord('a') + winner_coordinate[1])}{winner_coordinate[0] + 1}.")
