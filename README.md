# book-store-demo

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/siddjoshi/book-store-demo.git
   cd book-store-demo
   ```

2. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```sh
   flask run
   ```

## Usage Examples

### Add a Book
```sh
curl -X POST -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99, "quantity": 3}' http://127.0.0.1:5000/books
```

### View Books
```sh
curl http://127.0.0.1:5000/books
```

### Update a Book
```sh
curl -X PUT -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "price": 12.99}' http://127.0.0.1:5000/books/The%20Great%20Gatsby
```

### Delete a Book
```sh
curl -X DELETE http://127.0.0.1:5000/books/The%20Great%20Gatsby
```

### Search Books
```sh
curl http://127.0.0.1:5000/books/search?query=Gatsby
```

### View Summary Statistics
```sh
curl http://127.0.0.1:5000/books/summary
```

### Export Books to PDF
```sh
curl http://127.0.0.1:5000/books/export/pdf
```

### Export Books to Excel
```sh
curl http://127.0.0.1:5000/books/export/excel
```

## Code Comments

The code includes comments for clarity. Please refer to the `book_store.py` and `test_book_store.py` files for detailed explanations of each function and class.
