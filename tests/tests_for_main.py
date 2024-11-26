import unittest
from unittest.mock import patch
from io import StringIO
from app.library import LibraryManager
from app.main import run_cli


class TestLibraryCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=["1", "Test Book", "Test Author", "2024", "0"])  # Мок для input
    @patch('sys.stdout', new_callable=StringIO)  # Мок для stdout
    def test_add_book(self, mock_stdout, mock_input):
        """Тест: добавление книги"""

        # Создаем объект менеджера библиотеки
        manager = LibraryManager()

        # Запускаем функцию run_cli (в идеале, нужно бы её тоже переделать под возможность тестирования)
        run_cli()

        # Проверяем, что вывод содержит подтверждение добавления книги
        output = mock_stdout.getvalue()
        self.assertIn("Книга добавлена:", output)
        self.assertIn("Test Book", output)
        self.assertIn("Test Author", output)
        self.assertIn("2024", output)

    @patch('builtins.input', side_effect=["4", "0"])  # Показать все книги и выйти
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_books(self, mock_stdout, mock_input):
        """Тест: вывод всех книг"""

        # Создаем объект менеджера библиотеки
        manager = LibraryManager()

        # Добавляем несколько книг
        manager.add_book("Book 1", "Author 11", 2021)
        manager.add_book("Book 2", "Author 22", 2022)

        # Запускаем CLI для просмотра всех книг
        run_cli()

        # Проверяем, что в выводе содержатся добавленные книги
        output = mock_stdout.getvalue()
        self.assertIn("Book 1", output)
        self.assertIn("Author 11", output)
        self.assertIn("2021", output)
        self.assertIn("Book 2", output)
        self.assertIn("Author 22", output)
        self.assertIn("2022", output)

    @patch('builtins.input', side_effect=["2", "1", "0"])  # Удалить книгу с id 1 и выйти
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_book(self, mock_stdout, mock_input):
        """Тест: удаление книги"""

        # Создаем объект менеджера библиотеки
        manager = LibraryManager()

        # Добавляем книгу для удаления
        manager.add_book("Book to delete", "Author", 2021)

        # Запускаем функцию run_cli
        run_cli()

        # Проверяем, что вывод содержит информацию об успешном удалении
        output = mock_stdout.getvalue()
        self.assertIn("Книга успешно удалена.", output)

    @patch('builtins.input', side_effect=["3", "Test Book", "Test Author", "2024", "0"])  # Найти книгу
    @patch('sys.stdout', new_callable=StringIO)
    def test_find_books(self, mock_stdout, mock_input):
        """Тест: поиск книг"""

        # Создаем объект менеджера библиотеки
        manager = LibraryManager()

        # Добавляем книгу для поиска
        manager.add_book("Test Book", "Test Author", 2024)

        # Запускаем функцию run_cli
        run_cli()

        # Проверяем, что вывод содержит информацию о найденной книге
        output = mock_stdout.getvalue()
        self.assertIn("Test Book", output)
        self.assertIn("Test Author", output)
        self.assertIn("2024", output)


if __name__ == '__main__':
    unittest.main()
