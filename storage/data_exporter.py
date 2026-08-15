from storage.json_handler import JSONHandler
from storage.pickle_handler import PickleHandler
from exceptions.errors import StorageError

JSON = "json"
JSONL = "jsonl"
PICKLE = "pickle"


class DataExporter:
    @staticmethod
    def export(books, filepath, fmt):
        if fmt == PICKLE:
            PickleHandler.save(books, filepath)
        elif fmt == JSONL:
            JSONHandler.save_jsonl(books, filepath)
        elif fmt == JSON:
            JSONHandler.save(books, filepath)
        else:
            raise StorageError(f"Unknown format: {fmt}")

    @staticmethod
    def import_data(filepath, fmt):
        if fmt == PICKLE:
            return PickleHandler.load(filepath)
        elif fmt == JSONL:
            return JSONHandler.load_jsonl(filepath)
        elif fmt == JSON:
            return JSONHandler.load(filepath)
        else:
            raise StorageError(f"Unknown format: {fmt}")
