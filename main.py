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


def add_book(tracker):
    print("\n📘 Add a New Book\n")
    print("Book type:")
    print("1. Regular Book")
    print("2. EBook")
    print("3. AudioBook")
    type_choice = input("Enter choice (1-3): ").strip()

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    pages_raw = input("Enter total pages: ").strip()

    try:
        pages = int(pages_raw)
        data = {"title": title, "author": author, "genre": genre, "pages": pages}

        if type_choice == "2":
            file_size = float(input("Enter file size (MB): ").strip())
            EBook.validate_data({**data, "file_size": file_size})
            book = EBook(title, author, genre, pages, file_size)
        elif type_choice == "3":
            duration = int(input("Enter duration (minutes): ").strip())
            AudioBook.validate_data({**data, "duration_minutes": duration})
            book = AudioBook(title, author, genre, pages, duration)
        else:
            Book.validate_data(data)
            book = Book(title, author, genre, pages)

        tracker.add_book(book)
        print(f"\n✅ Book '{title}' added successfully!")
    except (ValueError, InvalidBookDataError) as e:
        print(f"\n❌ Could not add book: {e}")

    print("Returning to main menu...\n")


def view_books(tracker):
    print("\n📚 Your Library:\n")
    books = tracker.list_books()
    if not books:
        print("Your library is empty.")
    else:
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")
    print("\nReturning to main menu...\n")


def log_progress(tracker):
    print("\n📖 Log Reading Progress\n")
    title = input("Enter book title: ").strip()
    pages_raw = input("Enter pages read: ").strip()
    notes = input("Enter notes (optional): ").strip()

    try:
        pages = int(pages_raw)
        tracker.log_reading(title, pages, notes)
        print("\n✅ Reading log added!")
    except BookNotFoundError as e:
        print(f"\n❌ {e}")
    except (ValueError, InvalidLogError) as e:
        print(f"\n❌ Could not log reading progress: {e}")

    print("Returning to main menu...\n")


def view_progress(progress_manager):
    print("\n📈 Reading Progress:\n")
    print(progress_manager.generate_report())
    print("\nReturning to main menu...\n")


def export_data(tracker):
    print("\n📤 Export Book Data\n")
    print("Choose format:")
    print("1. JSON")
    print("2. Pickle")
    print("3. JSON Lines")
    choice = input("\nEnter your choice: ").strip()
    filename = input("Enter filename: ").strip()

    if choice == "2":
        fmt = PICKLE
    elif choice == "3":
        fmt = JSONL
    else:
        fmt = JSON

    try:
        DataExporter.export(tracker.list_books(), filename, fmt)
        print(f"\n✅ Data exported to '{filename}'")
    except StorageError as e:
        print(f"\n❌ Export failed: {e}")

    print("Returning to main menu...\n")


def import_data(tracker):
    print("\n📥 Import Book Data\n")
    filename = input("Enter filename: ").strip()

    if filename.endswith((".pkl", ".pickle")):
        fmt = PICKLE
    elif filename.endswith(".jsonl"):
        fmt = JSONL
    else:
        fmt = JSON

    try:
        books = DataExporter.import_data(filename, fmt)
        tracker.replace_books(books)
        print("\n✅ Books imported successfully!")
    except StorageError as e:
        print(f"\n❌ Import failed: {e}")

    print("Returning to main menu...\n")


def export_report(progress_manager):
    print("\n📝 Export Reading Report\n")
    filename = input("Enter filename (e.g. report.txt): ").strip()

    try:
        progress_manager.export_report(filename)
        print(f"\n✅ Reading report exported to '{filename}'")
    except StorageError as e:
        print(f"\n❌ Report export failed: {e}")

    print("Returning to main menu...\n")


def main():
    tracker = ReadingTracker()
    progress_manager = ProgressManager(tracker.list_books)

    print("🖥️  BookBuddy CLI")
    print("📚 Welcome to BookBuddy!")
    print("Track your reading, log progress, and manage your personal library.")

    actions = {
        "1": lambda: add_book(tracker),
        "2": lambda: view_books(tracker),
        "3": lambda: log_progress(tracker),
        "4": lambda: view_progress(progress_manager),
        "5": lambda: export_data(tracker),
        "6": lambda: import_data(tracker),
        "7": lambda: export_report(progress_manager),
    }

    while True:
        print(MENU)
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("\n👋 Thanks for using BookBuddy. Happy reading!")
            logger.info("Application exited by user.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("\n⚠️  Invalid choice, please enter a number between 1 and 8.\n")


if __name__ == "__main__":
    main()
