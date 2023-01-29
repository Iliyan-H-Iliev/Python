book_name = input()

book_count = 0

while True:
    input_book = input()

    if input_book == book_name:
        print(f"You checked {book_count} books and found it.")
        break

    if input_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break

    book_count += 1
