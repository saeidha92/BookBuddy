from models.book import Book
from models.ebook import EBook
from models.audiobook import AudioBook
from services.reading_tracker import ReadingTracker
from services.progress_manager import ProgressManager
from storage.data_exporter import DataExporter, JSON, JSONL, PICKLE
from exceptions.errors import (
    BookNotFoundError,
    InvalidBookDataError,
    InvalidLogError,
    StorageError,
)
from config.logger import logger

MENU = """
Main Menu:
1. Add a new book
2. View all books
3. Log reading progress
4. View reading progress
5. Export book data
6. Import book data
7. Export reading report
8. Exit
"""
