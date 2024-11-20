import unittest
import os
import json
from book_store import Book, BookStore, app

class TestBookStore(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.store = BookStore('test_books.json')
        self.store.books = []
        self.store.save_books()

    def tearDown(self):
        if os.path.exists('test_books.json'):
            os.remove('test_books.json')

    def test_add_book(self):
        response = self.app.post('/books', json={
            'title': 'Test Title',
            'author': 'Test Author',
            'price': 10.99,
            'quantity': 5
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(self.store.view_books()), 1)
        self.assertEqual(self.store.view_books()[0]['title'], 'Test Title')

    def test_view_books(self):
        book1 = Book('Test Title 1', 'Test Author 1', 10.99, 5)
        book2 = Book('Test Title 2', 'Test Author 2', 12.99, 3)
        self.store.add_book(book1)
        self.store.add_book(book2)
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]['title'], 'Test Title 1')
        self.assertEqual(books[1]['title'], 'Test Title 2')

    def test_update_book(self):
        book = Book('Test Title', 'Test Author', 10.99, 5)
        self.store.add_book(book)
        response = self.app.put('/books/Test Title', json={
            'title': 'Updated Title',
            'price': 15.99
        })
        self.assertEqual(response.status_code, 200)
        updated_book = self.store.view_books()[0]
        self.assertEqual(updated_book['title'], 'Updated Title')
        self.assertEqual(updated_book['price'], 15.99)

    def test_delete_book(self):
        book = Book('Test Title', 'Test Author', 10.99, 5)
        self.store.add_book(book)
        response = self.app.delete('/books/Test Title')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.store.view_books()), 0)

    def test_search_books(self):
        book1 = Book('Test Title 1', 'Test Author 1', 10.99, 5)
        book2 = Book('Another Title', 'Another Author', 12.99, 3)
        self.store.add_book(book1)
        self.store.add_book(book2)
        response = self.app.get('/books/search?query=Test')
        self.assertEqual(response.status_code, 200)
        results = json.loads(response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Test Title 1')
        response = self.app.get('/books/search?query=Another')
        self.assertEqual(response.status_code, 200)
        results = json.loads(response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Another Title')

    def test_get_summary_statistics(self):
        book1 = Book('Test Title 1', 'Test Author 1', 10.99, 5)
        book2 = Book('Test Title 2', 'Test Author 2', 12.99, 3)
        self.store.add_book(book1)
        self.store.add_book(book2)
        response = self.app.get('/books/summary')
        self.assertEqual(response.status_code, 200)
        stats = json.loads(response.data)
        self.assertEqual(stats['total_books'], 2)
        self.assertEqual(stats['total_inventory_value'], 10.99 * 5 + 12.99 * 3)

    def test_export_books_to_pdf(self):
        book1 = Book('Test Title 1', 'Test Author 1', 10.99, 5)
        book2 = Book('Test Title 2', 'Test Author 2', 12.99, 3)
        self.store.add_book(book1)
        self.store.add_book(book2)
        response = self.app.get('/books/export/pdf')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('books.pdf'))

    def test_export_books_to_excel(self):
        book1 = Book('Test Title 1', 'Test Author 1', 10.99, 5)
        book2 = Book('Test Title 2', 'Test Author 2', 12.99, 3)
        self.store.add_book(book1)
        self.store.add_book(book2)
        response = self.app.get('/books/export/excel')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('books.xlsx'))

if __name__ == '__main__':
    unittest.main()
