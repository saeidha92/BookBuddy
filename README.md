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