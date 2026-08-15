import json

from models.book import Book
from models.ebook import EBook
from models.audiobook import AudioBook
from utils.context import FileManager
from utils.retry import retry
from exceptions.errors import StorageError
from config.logger import logger

TYPE_MAP = {"Book": Book, "EBook": EBook, "AudioBook": AudioBook}


class JSONHandler:
    @staticmethod
    @retry(times=3)
    def save(books, filepath):
        try:
            data = [b.to_dict() for b in books]
            with FileManager(filepath, "w") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved {len(books)} books to {filepath}")
        except OSError as e:
            raise StorageError(f"Could not save JSON: {e}")

    @staticmethod
    @retry(times=3)
    def load(filepath):
        try:
            with FileManager(filepath, "r") as f:
                raw_data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            raise StorageError(f"Could not load JSON: {e}")

        books = []
        for item in raw_data:
            book_class = TYPE_MAP.get(item.get("type", "Book"), Book)
            books.append(book_class.from_dict(item))
        return books

    @staticmethod
    @retry(times=3)
    def save_jsonl(books, filepath):
        try:
            with FileManager(filepath, "w") as f:
                for b in books:
                    f.write(json.dumps(b.to_dict()) + "\n")
            logger.info(f"Saved {len(books)} books to {filepath} (JSON Lines)")
        except OSError as e:
            raise StorageError(f"Could not save JSON Lines: {e}")

    @staticmethod
    @retry(times=3)
    def load_jsonl(filepath):
        try:
            with FileManager(filepath, "r") as f:
                lines = [line.strip() for line in f if line.strip()]
        except OSError as e:
            raise StorageError(f"Could not load JSON Lines: {e}")

        books = []
        for line in lines:
            try:
                item = json.loads(line)
            except json.JSONDecodeError as e:
                raise StorageError(f"Invalid JSON Lines data: {e}")
            book_class = TYPE_MAP.get(item.get("type", "Book"), Book)
            books.append(book_class.from_dict(item))
        return books
