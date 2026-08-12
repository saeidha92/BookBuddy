# BookBuddy

BookBuddy is a simple command-line Python application for tracking your
reading habits. It lets you keep a personal library, log your reading
sessions, and see how much progress you've made on each book.

The idea behind it: a small startup called "BookBuddy" wants to help
readers stay consistent with reading. This project is the first step -
a CLI tool - with the long-term idea of eventually becoming a full web
app.

## What it does

- Add books to your library (title, author, genre, pages, date added)
- Supports three types of books: regular Book, EBook, and AudioBook
- Log reading sessions (date, pages read, notes)
- Track reading progress and see which books are completed
- Export and import your library as JSON or Pickle files
- Export a text report of your reading progress
- Handles errors properly and logs all actions to `bookbuddy.log`

## Project structure

```
bookbuddy/
├── models/       -> Book, EBook, AudioBook, ReadingLog classes
├── services/     -> reading tracker and progress manager (business logic)
├── storage/      -> JSON/Pickle save and load, and the data exporter
├── utils/        -> decorators, retry logic, and a file context manager
├── config/       -> logging setup
├── exceptions/   -> custom error classes
└── main.py       -> the CLI menu
```

## 🖥️ Demo

```
🖥️  BookBuddy CLI
📚 Welcome to BookBuddy!
Track your reading, log progress, and manage your personal library.

Main Menu:
1. Add a new book
2. View all books
3. Log reading progress
4. View reading progress
5. Export book data
6. Import book data
7. Export reading report
8. Exit

Enter your choice (1-8): 1

📘 Add a New Book

Enter book title: python
Enter author name: John Doe
Enter genre: Self-help
Enter total pages: 320

✅ Book 'python' added successfully!
```

```
📈 Reading Progress:

python - 40/320 pages read (12.5%)
The Hobbit - 0/310 pages read (0.0%)

Overall progress: 6.25%
Books completed: 0/2
```

