# BookBuddy

BookBuddy is a simple command-line Python application for tracking your
reading habits. It lets you keep a personal library, log your reading
sessions, and see how much progress you've made on each book.

The idea behind it: a small startup called "BookBuddy" wants to help
readers stay consistent with reading. This project is the first step -
a CLI tool - with the long-term idea of eventually becoming a full web
app.

![BookBuddy demo](./assets/demo.gif)

## What it does

- Add books to your library (title, author, genre, pages, date added)
- Supports three types of books: regular Book, EBook, and AudioBook
- Log reading sessions (date, pages read, notes)
- Track reading progress and see which books are completed
- Export and import your library as JSON or Pickle files
- Export a text report of your reading progress
- Handles errors properly and logs all actions to `bookbuddy.log`

## 🏗️ Project Architecture

```
bookbuddy/
│
├── models/                  # Core data classes (OOP layer)
│   ├── book.py                  Book (base class) + Readable ABC interface
│   ├── ebook.py                 EBook(Book)   — adds file_size
│   ├── audiobook.py             AudioBook(Book) — adds duration_minutes
│   └── reading_log.py           ReadingLog — one reading session
│
├── services/                # Business logic layer
│   ├── reading_tracker.py       Owns the book collection, logs sessions
│   └── progress_manager.py      Progress statistics & report generation
│
├── storage/                 # Persistence layer
│   ├── json_handler.py          Save/load books as JSON
│   ├── pickle_handler.py        Save/load books as Pickle
│   └── data_exporter.py         Facade over both handlers
│
├── utils/                   # Reusable helpers
│   ├── decorators.py            @log_action, @timing
│   ├── context.py               FileManager (safe file I/O)
│   └── retry.py                 @retry decorator
│
├── config/
│   └── logger.py             Centralized logging configuration
│
├── exceptions/
│   └── errors.py             Custom exception hierarchy
│
├── .venv/                    Python virtual environment
├── requirements.txt          Dependencies (standard library only)
└── main.py                   CLI entry point
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

---

## 🚀 Getting Started

### Requirements

Python **3.9+**. No third-party packages — only the standard library.

### 1. Extract the project

Unzip the provided archive; you'll get a `bookbuddy/` folder.

### 2. Activate the virtual environment

**macOS / Linux**

```bash
cd bookbuddy
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
cd bookbuddy
.venv\Scripts\Activate.ps1
```

> If `.venv` doesn't work on your machine (e.g. different OS), recreate it:
>
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate   # or the Windows equivalent above
> ```

### 3. Run the app

```bash
python main.py
```

---

## 📋 Usage Guide

| Menu option                  | What it does                                                      |
| ---------------------------- | ----------------------------------------------------------------- |
| **1. Add a new book**        | Choose a type (Regular / EBook / AudioBook) and enter its details |
| **2. View all books**        | Lists every book in your library with type-specific details       |
| **3. Log reading progress**  | Records a reading session and updates that book's progress        |
| **4. View reading progress** | Shows per-book and overall progress statistics                    |
| **5. Export book data**      | Saves your whole library to a JSON or Pickle file                 |
| **6. Import book data**      | Loads a library from a previously exported file                   |
| **7. Export reading report** | Writes the progress report to a `.txt` file                       |
| **8. Exit**                  | Closes the app                                                    |

---

## A note on Pickle

Pickle files should only be imported if you created them yourself with
this program - loading a Pickle file from somewhere else can run
unsafe code.

## Logging

Every action and error gets logged to `bookbuddy.log`, so if something
goes wrong you can check that file to see what happened.
