import unittest
import os
import json
from book_store import Book, BookStore

class TestBookStore(unittest.TestCase):
    def setUp(self):
        self.store = BookStore('test_books.json')
        self.store.books = []
        self.store.save_books()

    def tearDown(self):
        if os.path.exists('test_books.json'):
            os.remove('test_books.json')

    def test_add_book(self):
        book = Book("Test Title", "Test Author", 10.99, 5)
        self.store.add_book(book)
        self.assertEqual(len(self.store.view_books()), 1)
        self.assertEqual(self.store.view_books()[0]['title'], "Test Title")

    def test_view_books(self):
        book1 = Book("Test Title 1", "Test Author 1", 10.99, 5)
        book2 = Book("Test Title 2", "Test Author 2", 12.99, 3)
        self.store.add_book(book1)
        self.store.add_book(book2)
        books = self.store.view_books()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]['title'], "Test Title 1")
        self.assertEqual(books[1]['title'], "Test Title 2")

    def test_update_book(self):
        book = Book("Test Title", "Test Author", 10.99, 5)
        self.store.add_book(book)
        self.store.update_book("Test Title", {"title": "Updated Title", "price": 15.99})
        updated_book = self.store.view_books()[0]
        self.assertEqual(updated_book['title'], "Updated Title")
        self.assertEqual(updated_book['price'], 15.99)

    def test_delete_book(self):
        book = Book("Test Title", "Test Author", 10.99, 5)
        self.store.add_book(book)
        self.store.delete_book("Test Title")
        self.assertEqual(len(self.store.view_books()), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Book("Test Title", "Test Author", "invalid_price", 5)

    def test_empty_inventory(self):
        self.assertEqual(len(self.store.view_books()), 0)

if __name__ == '__main__':
    unittest.main()
