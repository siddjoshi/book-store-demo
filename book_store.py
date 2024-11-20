import json
import os
from flask import Flask, request, jsonify
from fpdf import FPDF
import pandas as pd

class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

class BookStore:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book):
        self.books.append(book.__dict__)
        self.save_books()

    def view_books(self):
        return self.books

    def update_book(self, title, new_details):
        for book in self.books:
            if book['title'] == title:
                book.update(new_details)
                self.save_books()
                return True
        return False

    def delete_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
                results.append(book)
        return results

    def get_summary_statistics(self):
        total_books = len(self.books)
        total_inventory_value = sum(book['price'] * book['quantity'] for book in self.books)
        return {
            'total_books': total_books,
            'total_inventory_value': total_inventory_value
        }

    def export_books_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for book in self.books:
            pdf.cell(200, 10, txt=f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}", ln=True)
        pdf.output("books.pdf")

    def export_books_to_excel(self):
        df = pd.DataFrame(self.books)
        df.to_excel("books.xlsx", index=False)

app = Flask(__name__)
store = BookStore()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(data['title'], data['author'], data['price'], data['quantity'])
    store.add_book(book)
    return jsonify({'message': 'Book added successfully!'}), 201

@app.route('/books', methods=['GET'])
def view_books():
    books = store.view_books()
    return jsonify(books), 200

@app.route('/books/<title>', methods=['PUT'])
def update_book(title):
    new_details = request.get_json()
    if store.update_book(title, new_details):
        return jsonify({'message': 'Book updated successfully!'}), 200
    return jsonify({'message': 'Book not found.'}), 404

@app.route('/books/<title>', methods=['DELETE'])
def delete_book(title):
    if store.delete_book(title):
        return jsonify({'message': 'Book deleted successfully!'}), 200
    return jsonify({'message': 'Book not found.'}), 404

@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    results = store.search_books(query)
    return jsonify(results), 200

@app.route('/books/summary', methods=['GET'])
def get_summary_statistics():
    stats = store.get_summary_statistics()
    return jsonify(stats), 200

@app.route('/books/export/pdf', methods=['GET'])
def export_books_to_pdf():
    store.export_books_to_pdf()
    return jsonify({'message': 'Books exported to PDF successfully!'}), 200

@app.route('/books/export/excel', methods=['GET'])
def export_books_to_excel():
    store.export_books_to_excel()
    return jsonify({'message': 'Books exported to Excel successfully!'}), 200

if __name__ == "__main__":
    app.run(debug=True)
