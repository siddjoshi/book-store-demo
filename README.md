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
   python book_store.py
   ```

## Usage Examples

### Add a Book
```sh
Enter your choice: 1
Enter title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter price: 10.99
Enter quantity: 3
Book added successfully!
```

### View Books
```sh
Enter your choice: 2
Title: The Great Gatsby, Author: F. Scott Fitzgerald, Price: 10.99, Quantity: 3
```

### Update a Book
```sh
Enter your choice: 3
Enter the title of the book to update: The Great Gatsby
Enter new title (leave blank to keep current): 
Enter new author (leave blank to keep current): 
Enter new price (leave blank to keep current): 12.99
Enter new quantity (leave blank to keep current): 
Book updated successfully!
```

### Delete a Book
```sh
Enter your choice: 4
Enter the title of the book to delete: The Great Gatsby
Book deleted successfully!
```

## Code Comments

The code includes comments for clarity. Please refer to the `book_store.py` and `test_book_store.py` files for detailed explanations of each function and class.
