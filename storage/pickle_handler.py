import pickle

from utils.context import FileManager
from utils.retry import retry
from exceptions.errors import StorageError
from config.logger import logger


class PickleHandler:
    @staticmethod
    @retry(times=3)
    def save(books, filepath):
        try:
            with FileManager(filepath, "wb") as f:
                pickle.dump(books, f)
            logger.info(f"Saved {len(books)} books to {filepath}")
        except OSError as e:
            raise StorageError(f"Could not save pickle: {e}")

    @staticmethod
    @retry(times=3)
    def load(filepath):
        try:
            with FileManager(filepath, "rb") as f:
                return pickle.load(f)
        except OSError as e:
            raise StorageError(f"Could not load pickle: {e}")
