n = int(input())

key_by_piece = {}
composer_by_piece = {}

for i in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]

    composer_by_piece[piece] = composer
    key_by_piece[piece] = key

while True:
    data = input().split("|")

    command = data[0]

    if command == "Stop":
        break

    piece = data[1]

    if command == "Add":
        composer = data[2]
        key = data[3]

        if piece not in composer_by_piece:
            composer_by_piece[piece] = composer
            key_by_piece[piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command == "Remove":
        if piece not in composer_by_piece:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            composer_by_piece.pop(piece)
            key_by_piece.pop(piece)
            print(f"Successfully removed {piece}!")

    elif command == "ChangeKey":
        new_key = data[2]
        if piece not in composer_by_piece:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            key_by_piece[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for k in composer_by_piece.keys():
    print(f"{k} -> Composer: {composer_by_piece[k]}, Key: {key_by_piece[k]}")
