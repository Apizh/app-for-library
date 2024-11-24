import unittest
from app.library import LibraryManager, STORAGE_FILE
from pathlib import Path


class TestLibrary(unittest.TestCase):
    """Тестирование создания файла хранения библиотеки."""

    def test_path_creation(self):
        """Тест: Проверка создания пути файла без передачи пути"""
        file_path = LibraryManager()
        self.assertTrue(str(file_path.storage_file).endswith('library.json'))

    def test_incorrect_path_creation(self):
        """Тест: Передаём некорректный путь, на выходе получаем обработку этого пути"""
        file_path = LibraryManager("/некорректный путь/").storage_file
        self.assertNotEqual(file_path, STORAGE_FILE)
        self.assertTrue(str(file_path).endswith('library.json'))

    def test_input_path(self):
        """Тест: указание существующей директории(абсолютный путь) на выходе
        полный путь к файлу 'директория/library.json'"""
        adress = r"C:\Users\admin\PycharmProjects\library-app"
        file_path = LibraryManager(adress).storage_file
        # Проверяем что это не файл
        self.assertFalse(file_path.is_file())
        # Проверка создания абсолютного пути к файлу adress + library.json
        self.assertEqual(str(file_path), adress + '\library.json')