from abc import ABC, abstractmethod
from datetime import date
from typing import Optional


class Readable(ABC):

    @abstractmethod
    def mark_read_page(self, pages: int):
        raise NotImplementedError

    @property
    @abstractmethod
    def reading_progress(self):
        raise NotImplementedError


class Book(Readable):
    def __init__(self, title: str, author: str, genre: str, pages: int, date_added: Optional[date] = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.date_added = date_added or date.today()
        self.__pages_read = 0
        self.reading_logs = []

        Book.total_books_created += 1

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
