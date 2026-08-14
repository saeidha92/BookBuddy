from datetime import date

class ReadingLog:
    def __init__(self, pages_read, log_date=None, notes=""):
        if pages_read < 0:
            raise InvalidLogError("Pages read cannot be negative.")
        self.pages_read = pages_read
        self.log_date = log_date or date.today()
        self.notes = notes

    def to_dict(self):
        return {
            "pages_read": self.pages_read,
            "log_date": self.log_date.isoformat(),
            "notes": self.notes,
        }

    def __str__(self):
        note = f" - {self.notes}" if self.notes else ""
        return f"[{self.log_date}] +{self.pages_read} pages{note}"
