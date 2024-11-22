import json
from typing import Optional, List
from book import Book, ValidationError


class LibraryManager:
    def __init__(self, storage_file: str = "library.json"):
        self.storage_file = storage_file
        self.books: List[Book] = []
        self._load_books()

    def _load_books(self):
        """Load books from the storage file."""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def _save_books(self):
        """Save books to the storage file."""
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Book:
        """Add a new book to the library."""
        new_id = max((book.id for book in self.books), default=0) + 1
        try:
            new_book = Book(id=new_id, title=title, author=author, year=year)
        except ValidationError as e:
            print(f"Ошибка добавления книги: {e}")
            return None
        self.books.append(new_book)
        self._save_books()
        return new_book

    def delete_book(self, book_id: int) -> bool:
        """Delete a book by its ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self._save_books()
                return True
        return False

    def find_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None) -> List[
        Book]:
        """Find books by title, author, or year."""
        return [
            book for book in self.books
            if (title is None or title.lower() in book.title.lower())
               and (author is None or author.lower() in book.author.lower())
               and (year is None or book.year == year)
        ]

    def list_books(self) -> List[Book]:
        """List all books in the library."""
        return self.books

    def update_status(self, book_id: int, new_status: str) -> bool:
        """Update the status of a book."""
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self._save_books()
                return True
        return False
