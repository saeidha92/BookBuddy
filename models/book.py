from abc import ABC, abstractmethod
from datetime import date

from exceptions.errors import InvalidBookDataError


class Readable(ABC):
    """Any book type must be able to mark pages as read and show progress."""

    @abstractmethod
    def mark_read_pages(self, pages):
        pass

    @property
    @abstractmethod
    def reading_progress(self):
        pass


class Book(Readable):
    def __init__(self, title, author, genre, pages, date_added=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.date_added = date_added or date.today()

        # private attribute
        self.__pages_read = 0
        self.reading_logs = []

    @property
    def pages_read(self):
        return self.__pages_read

    @property
    def reading_progress(self):
        if self.pages <= 0:
            return 0.0
        return round((self.__pages_read / self.pages) * 100, 2)

    @property
    def is_completed(self):
        return self.__pages_read >= self.pages

    def mark_read_pages(self, pages):
        if pages < 0:
            raise InvalidBookDataError("Pages read cannot be negative.")
        self.__pages_read = min(self.pages, self.__pages_read + pages)

    def add_log(self, reading_log):
        self.reading_logs.append(reading_log)
        self.mark_read_pages(reading_log.pages_read)

    def summary(self):
        return f"{self.title} by {self.author} [{self.genre}] - {self.pages} pages ({self.reading_progress}% read)"

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages,
            "date_added": self.date_added.isoformat(),
            "pages_read": self.pages_read,
        }

    @classmethod
    def from_dict(cls, data):
        cls.validate_data(data)
        added = (
            date.fromisoformat(data["date_added"])
            if data.get("date_added")
            else date.today()
        )
        book = cls(
            data["title"], data["author"], data["genre"], int(data["pages"]), added
        )
        if data.get("pages_read"):
            book.mark_read_pages(int(data["pages_read"]))
        return book

    @staticmethod
    def validate_data(data):
        for field in ("title", "author", "genre", "pages"):
            if field not in data or data[field] in (None, ""):
                raise InvalidBookDataError(f"Missing field: {field}")
        try:
            pages = int(data["pages"])
        except (TypeError, ValueError):
            raise InvalidBookDataError("'pages' must be an integer.")
        if pages <= 0:
            raise InvalidBookDataError("'pages' must be positive.")

    def __str__(self):
        return self.summary()
