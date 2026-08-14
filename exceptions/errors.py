class BookBuddyError(Exception):
    """Base class for all our custom errors."""

    pass


class BookNotFoundError(BookBuddyError):
    """Shows when a book title is not found in the library."""

    def __init__(self, title):
        self.title = title
        super().__init__(f"Book '{title}' was not found.")


class InvalidLogError(BookBuddyError):
    """shows when a reading log has bad data (e.g. negative pages)."""

    def __init__(self, message="Invalid reading log data."):
        super().__init__(message)


class InvalidBookDataError(BookBuddyError):
    """Shows when book data is missing fields or invalid."""

    def __init__(self, message="Invalid book data."):
        super().__init__(message)


class StorageError(BookBuddyError):
    """Shows when saving or loading a file fails."""

    pass
