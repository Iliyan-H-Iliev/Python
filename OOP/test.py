from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"This is a book with title - ' {self.title} ' written by {self.author}."


class Library:
    def __init__(self, name):
        self.name = name
        self.books: List = [Book]

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            return f"Book with title {book.title} and author {book.author} successfully added to {self.name} library"

        return f"This book is already in the library!"

    def find_book(self, title):
        try:
            curr_book = next(filter(lambda b: b.title == title, self.books))
            return curr_book
        except StopIteration:
            raise ValueError("This book is not in the library")


a = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling")
library = Library("Downtown")
print(library.add_book(a))
print(library.add_book(a))
print(library.find_book("Harry Potter and the Philosopher's Stone"))
