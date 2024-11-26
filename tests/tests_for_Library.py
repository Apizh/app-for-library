import unittest
from app.library import LibraryManager, STORAGE_FILE


class TestLibrary(unittest.TestCase):
    """Тестирование создания файла хранения библиотеки."""

    def test_path_creation(self):
        """Тест: Проверка корректного создания пути файла без указания пути."""
        file_path = LibraryManager()
        self.assertTrue(str(file_path.storage_file).endswith('library.json'))

    def test_incorrect_path_creation(self):
        """Тест: Передача некорректного пути, ожидаемый результат — использование пути по умолчанию."""
        file_path = LibraryManager("\\некорректный путь\\").storage_file
        self.assertNotEqual(file_path, STORAGE_FILE)
        self.assertTrue(str(file_path).endswith('library.json'))

    def test_input_path(self):
        r"""Тест: указание существующего абсолютного пути к директории.
        Ожидаемый результат: путь к файлу должен быть 'директория\library.json'."""
        test_path = r"C:\Users\admin\PycharmProjects\library-app"
        file_path = LibraryManager(test_path).storage_file
        # Проверяем что это не файл
        # self.assertFalse(file_path.is_file())
        # Проверка создания абсолютного пути к файлу adress + \library.json
        self.assertEqual(str(file_path), test_path + r'\library.json')


if __name__ == '__main__':
    unittest.main()
