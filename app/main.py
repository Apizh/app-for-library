from typing import List
from app.book import Book
from app.library import LibraryManager


def run_cli():
    """Command-line interface for the library manager."""
    manager = LibraryManager()

    def print_books(books: List[Book]):
        """Print a list of books."""
        if not books:
            print("Книг не найдено.")
            return
        print(f"{'ID':<5} | {'Название':<30} | {'Автор':<20} | {'Год':<4} | {'Статус':<9}")
        print("-" * 80)
        for book in books:
            print(f"{book.id:<5} | {book.title:<30} | {book.author:<20} | {book.year:<4} | {book.status:<9}")
        print('Конец списка книг')

    while True:
        print("*** Система управления библиотекой ***")
        print("1. Добавить книгу",
              "2. Удалить книгу",
              '3. Найти книги',
              '4. Показать все книги',
              '5. Изменить статус книги',
              '0. Выйти', sep="\n")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            try:
                year = int(input("Введите год издания книги: ").strip())
                book = manager.add_book(title, author, year)
                if book:
                    print(f"Книга добавлена: {book.__dict__}")
            except ValueError:
                print("Год должен быть числом.")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: ").strip())
                if manager.delete_book(book_id):
                    print("Книга успешно удалена.")
                else:
                    print("Книга с указанным ID не найдена.")
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "3":
            title = input("Введите название книги для поиска (или оставьте пустым): ").strip()
            author = input("Введите автора книги для поиска (или оставьте пустым): ").strip()
            year_input = input("Введите год издания книги для поиска (или оставьте пустым): ").strip()
            year = int(year_input) if year_input.isdigit() else None
            books = manager.find_books(title=title or None, author=author or None, year=year)
            print_books(books)

        elif choice == "4":
            books = manager.list_books()
            print_books(books)
            print(80 * '-')

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги для изменения статуса: ").strip())
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
                if new_status not in ["в наличии", "выдана"]:
                    print('Некорректный статус. Используйте "в наличии" или "выдана".')
                    continue
                if manager.update_status(book_id, new_status):
                    print("Статус книги успешно обновлен.")
                else:
                    print("Книга с указанным ID не найдена.")
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор. Пожалуйста, повторите.")

if __name__ == "__main__":
    run_cli()
