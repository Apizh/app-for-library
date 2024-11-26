import json
from typing import Optional, List
from app.book import Book, ValidationError
from pathlib import Path

STORAGE_FILE = "library"


class LibraryManager:
    """
    Класс для управления коллекцией книг, загрузкой, добавлением,
    удалением, выводом содержимого из .json файла.
    """

    def __init__(self, storage_file: str = STORAGE_FILE):
        self.storage_file = self._valid_path(Path(storage_file))
        self.books: List[Book] = []
        self._load_books()

    def _valid_path(self, path_file: Path) -> Path:
        """Функция валидации пути к файлу/папке хранилища"""
        if path_file.suffix == ".json":
            if path_file.exists():
                # Если файл существует
                return path_file
            if '/' not in path_file.as_posix():
                # Если это название файла с расширением ".json"
                return path_file

            # Указанный путь {path_file} - неправильный.
            # В директории расположения скрипта будет создан файл 'library.json'
            # для работы с данными
            return Path('library.json').resolve()
        if path_file.exists():
            # Если это существующая директория в ней будет создан файл 'library.json'
            return path_file / 'library.json'

        # Если введены некорректные данные или путь не существует, будет создан файл
        # "library.json" в директории скрипта.
        return Path('library.json').resolve()

    def _load_books(self):
        """Load books from the storage file."""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print(f'Ошибка чтения файла: "{self.storage_file}".\nСоздан файл library.json для хранения данных.')
            self.books = []

    def _save_books(self):
        """Save books to the storage file."""
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Book | None:
        """Add a new book to the library."""
        new_id = 1  # Начинаем с 1, если список пуст

        if self.books:
            # Сортируем книги по id, чтобы гарантировать правильный порядок
            self.books.sort(key=lambda book: book.id)
            for i, book in enumerate(self.books, start=1):  # Перебор с индексацией с 1
                if book.id != i:  # Ищем пропуск
                    new_id = i  # Пропуск найден, присваиваем новый id
                    break
            else:
                # Если пропусков не найдено, новый id будет следующим за последним
                new_id = i + 1
        try:
            new_book = Book(id=new_id, title=title, author=author, year=year)
        except ValidationError as e:
            print(f"Ошибка добавления книги: {e}")
            return None

        self.books.append(new_book)
        self._save_books()
        return new_book

    def delete_book(self, book_id: int) -> bool:
        """Delete a book by its id."""
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
