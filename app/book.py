from datetime import datetime
from re import match


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class Book:
    """Represents a book with validation on initialization."""

    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = self.validate_title(title)
        self.author = self.validate_author(author)
        self.year = self.validate_year(year)
        self.status = status

    @staticmethod
    def validate_title(title: str) -> str:
        title = title.strip()
        pattern = r"^[a-zA-Zа-яА-ЯёЁ\s\-\'\".,;!?(){}[\]:]*[a-zA-Zа-яА-ЯёЁ]+[a-zA-Zа-яА-ЯёЁ\s\-\'\".,;!?(){}[\]:]*$"
        if not match(pattern, title) or len(title) > 50:
            raise ValidationError(
                "Название книги должно содержать от 1 до 50 символов, но не менее 1-й буквы в начале.")
        return title

    @staticmethod
    def validate_author(author: str) -> str:
        author = author.strip()
        valid_author = author.split()
        if not (all(map(str.isalpha, valid_author)) and 51 > len(author) > 4):
            raise ValidationError(
                "Имя автора должно состоять от 2 до 5 слов состоящих из букв от 2 до 10 разделённых пробелами включая границы диапазонов.")
        return author

    @staticmethod
    def validate_year(year: int) -> int:
        if not isinstance(year, int) or year < 0:
            raise ValidationError("Год издания должен быть целым положительным числом.")
        current_year = datetime.now().year
        if not (1899 < year <= current_year):
            raise ValidationError(
                f"Год издания должен быть в диапазоне от 1900 до {current_year} включая границы диапазона.")
        return year

    def to_dict(self):
        """Convert the book to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a book instance from a dictionary."""
        return cls(**data)


if __name__ == '__main__':
    print(Book.validate_author('   '))
