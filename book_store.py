import json
import os

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

def main():
    store = BookStore()

    while True:
        print("\nBook Store CLI")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            book = Book(title, author, price, quantity)
            store.add_book(book)
            print("Book added successfully!")

        elif choice == '2':
            books = store.view_books()
            if books:
                for book in books:
                    print(f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}")
            else:
                print("No books available.")

        elif choice == '3':
            title = input("Enter the title of the book to update: ")
            new_title = input("Enter new title (leave blank to keep current): ")
            new_author = input("Enter new author (leave blank to keep current): ")
            new_price = input("Enter new price (leave blank to keep current): ")
            new_quantity = input("Enter new quantity (leave blank to keep current): ")

            new_details = {}
            if new_title:
                new_details['title'] = new_title
            if new_author:
                new_details['author'] = new_author
            if new_price:
                new_details['price'] = float(new_price)
            if new_quantity:
                new_details['quantity'] = int(new_quantity)

            if store.update_book(title, new_details):
                print("Book updated successfully!")
            else:
                print("Book not found.")

        elif choice == '4':
            title = input("Enter the title of the book to delete: ")
            if store.delete_book(title):
                print("Book deleted successfully!")
            else:
                print("Book not found.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
