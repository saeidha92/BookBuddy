from models.reading_log import ReadingLog
from exceptions.errors import BookNotFoundError
from utils.decorators import log_action
from config.logger import logger


class ReadingTracker:
    def __init__(self):
        self._books = {}  # key: lowercase title, value: Book

    @log_action
    def add_book(self, book):
        self._books[book.title.lower()] = book

    @log_action
    def get_book(self, title):
        book = self._books.get(title.lower())
        if book is None:
            raise BookNotFoundError(title)
        return book

    def list_books(self):
        return list(self._books.values())

    @log_action
    def log_reading(self, title, pages_read, notes=""):
        book = self.get_book(title)
        entry = ReadingLog(pages_read, notes=notes)
        book.add_log(entry)
        logger.info(f"Logged {pages_read} pages for '{book.title}'")
        return entry

    def replace_books(self, books):
        self._books = {b.title.lower(): b for b in books}
