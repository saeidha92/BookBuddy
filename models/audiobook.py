from datetime import date

from models.book import Book


class AudioBook(Book):
    def __init__(self, title, author, genre, pages, duration_minutes, date_added=None):
        super().__init__(title, author, genre, pages, date_added)
        self.duration_minutes = duration_minutes

    def to_dict(self):
        data = super().to_dict()
        data["duration_minutes"] = self.duration_minutes
        return data

    @classmethod
    def from_dict(cls, data):
        cls.validate_data(data)
        added = (
            date.fromisoformat(data["date_added"])
            if data.get("date_added")
            else date.today()
        )
        book = cls(
            data["title"],
            data["author"],
            data["genre"],
            int(data["pages"]),
            int(data.get("duration_minutes", 0)),
            added,
        )
        if data.get("pages_read"):
            book.mark_read_pages(int(data["pages_read"]))
        return book

    @staticmethod
    def validate_data(data):
        Book.validate_data(data)
        if "duration_minutes" in data and int(data["duration_minutes"]) < 0:
            raise InvalidBookDataError("'duration_minutes' cannot be negative.")

    def summary(self):
        hours = self.duration_minutes // 60
        minutes = self.duration_minutes % 60
        return f"{super().summary()} [AudioBook, {hours}h {minutes}m]"
