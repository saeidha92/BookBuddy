from utils.context import FileManager
from utils.decorators import log_action
from exceptions.errors import StorageError


class ProgressManager:
    def __init__(self, books_provider):
        self._books_provider = books_provider

    def get_books(self):
        return self._books_provider()

    def overall_progress(self):
        books = self.get_books()
        if not books:
            return 0.0
        return round(sum(b.reading_progress for b in books) / len(books), 2)

    def completed_books(self):
        return [b for b in self.get_books() if b.is_completed]

    def generate_report(self):
        books = self.get_books()
        if not books:
            return "No books in the library yet."

        lines = []
        for b in books:
            lines.append(f"{b.title} - {b.pages_read}/{b.pages} pages read ({b.reading_progress}%)")
        lines.append("")
        lines.append(f"Overall progress: {self.overall_progress()}%")
        lines.append(f"Books completed: {len(self.completed_books())}/{len(books)}")
        return "\n".join(lines)

    @log_action
    def export_report(self, filepath):
        try:
            with FileManager(filepath, "w") as f:
                f.write(self.generate_report())
        except OSError as e:
            raise StorageError(f"Could not export report: {e}")
