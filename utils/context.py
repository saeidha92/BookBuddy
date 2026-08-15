from config.logger import logger


class FileManager:
    def __init__(self, filepath, mode="r"):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, self.mode, encoding="utf-8" if "b" not in self.mode else None)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            logger.error(f"Error while working with {self.filepath}: {exc_val}")
        return False
