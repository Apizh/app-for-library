from app.book import Book, ValidationError
import unittest


class TestBook(unittest.TestCase):
    """Testing the creation of the Book class and validating the data"""

    def test_initialization_class(self):
        """Тест: Проверка создания класса Book и правильного объявления атрибутов экземпляра класса."""
        first = Book(1, 'Так говорил Заратустра', 'Фридрих Ницше', 1900)
        self.assertEqual(first.id, 1)
        self.assertEqual(first.title, 'Так говорил Заратустра')
        self.assertEqual(first.author, 'Фридрих Ницше')
        self.assertEqual(first.year, 1900)
        self.assertIsInstance(first, Book)

    def test_initialization_invalid_author(self):
        """Тест: Проверка обработки некорректного ввода данных автора"""
        with self.assertRaises(ValidationError):
            Book.validate_author('12345')

    def test_initialization_invalid_title(self):
        """Тест: Проверка обработки некорректных данных названия книги"""
        with self.assertRaises(ValidationError):
            Book.validate_author('ав')

    def test_initialization_invalid_year(self):
        """Тест: Проверка обработки некорректных данных для поля year"""
        with self.assertRaises(ValidationError):
            Book.validate_year(1500)


if __name__ == '__main__':
    unittest.main()
