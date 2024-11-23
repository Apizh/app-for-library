import unittest
from app.library import LibraryManager, STORAGE_FILE
from pathlib import Path


class TestLibrary(unittest.TestCase):
    """Тестирование создания файла хранения библиотеки."""

    def test_path_creation(self):
        """Тест: Проверка создания пути файла"""
        file_exists = LibraryManager()
        self.assertEqual(file_exists.storage_file, STORAGE_FILE)
        self.assertTrue(str(file_exists.storage_file).endswith('library.json'))

    def test_incorrect_path_creation(self):
        """Тест: Передаём некорректный путь, на выходе получаем обработку этого пути"""
        file_exists = LibraryManager("/некорректный путь/").storage_file
        self.assertNotEqual(file_exists, STORAGE_FILE)
        self.assertTrue(str(file_exists).endswith('library.json'))
