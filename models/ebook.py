from datetime import date

from models.book import Book
from exceptions.errors import InvalidBookDataError


class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size, date_added=None):
        super().__init__(title, author, genre, pages, date_added)
        self.file_size = file_size  # in MB

    def to_dict(self):
        data = super().to_dict()
        data["file_size"] = self.file_size
        return data

    @classmethod
    def from_dict(cls, data):
        cls.validate_data(data)
        added = date.fromisoformat(data["date_added"]) if data.get("date_added") else date.today()
        book = cls(data["title"], data["author"], data["genre"], int(data["pages"]),
                    float(data.get("file_size", 0)), added)
        if data.get("pages_read"):
            book.mark_read_pages(int(data["pages_read"]))
        return book

    @staticmethod
    def validate_data(data):
        Book.validate_data(data)
        if "file_size" in data and float(data["file_size"]) < 0:
            raise InvalidBookDataError("'file_size' cannot be negative.")

    def summary(self):
        return f"{super().summary()} [EBook, {self.file_size} MB]"
