from project.bookstore import Bookstore
from unittest import TestCase, main

class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.book = Bookstore(5)

    def test_init(self):
        self.assertEquals(5, self.book.books_limit)
        self.assertEquals({}, self.book.availability_in_store_by_book_titles)
        self.assertEquals(0, self.book.total_sold_books)

    def test_privet_attribute_total_sold_books(self):
        self.assertEquals(0, self.book._Bookstore__total_sold_books)

    def test_privet_attribute_total_sold_books2(self):
        self.book._Bookstore__total_sold_books = 5
        self.assertEquals(5, self.book._Bookstore__total_sold_books)

    def test_privet_attribute_total_sold_books_with_error(self):
        with self.assertRaises(AttributeError):
            self.book.total_sold_books = 5
        self.assertEquals(0, self.book._Bookstore__total_sold_books)

    def test_books_limit_setter_with_value_under_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.book.books_limit = -5
        self.assertEqual("Books limit of -5 is not valid", str(ex.exception))

    def test_books_limit_setter_with_value_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.book.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_len(self):
        self.assertEquals(0, len(self.book))

    def test_len_with_books(self):
        self.book.availability_in_store_by_book_titles = {"test": 5, "test2": 4}
        self.assertEquals(9, len(self.book))