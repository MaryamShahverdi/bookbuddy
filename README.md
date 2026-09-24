## BookBuddy 📚

A personal library and reading-progress tracker built with Python. Add books, log your reading sessions, track your progress, and export/import your library as JSON.

## ✨ Features

- 📖 **Add books** with title, author, genre, and total page count
- 📈 **Log reading progress** — record pages read per session along with notes
- 📊 **View progress** — see how far you've read in each book, as a percentage
- 💾 **Export/Import** your entire library to/from a JSON file, so your data isn't lost between sessions
- 🎧 Support for different book types (`Book`, `Audiobook`) through a shared model structure
- ⚠️ Custom exceptions (`BookNotFoundError`, `InvalidLogError`, `StorageError`) for clear, predictable error handling

## 🏗️ Project structure

```
book_body/
├── main.py                    → CLI entry point
├── models/
│   ├── book.py                → Book model
│   ├── audiobook.py           → Audiobook model
│   └── reading_log.py         → A single reading session log
├── services/
│   └── reading_tracker.py     → Core logic: adding books, logging progress
├── storage/
│   ├── json_handler.py        → Low-level JSON read/write
│   └── data_exporter.py       → Export/import the whole library
├── exceptions/
│   └── errors.py              → Custom exception classes
├── config/
│   └── logger.py              → Logging configuration
└── utils/
    ├── decorators.py
    ├── retry.py
    └── context.py
```

## 🚀 Usage

```bash
python main.py
```

You'll see a menu with options to add books, view your library, log reading progress, view progress, and export/import your data.

## 💡 Example

```
Welcome to BookBuddy!
Track your reading, log progress, and manage your personal library.

Main Menu:
1. Add a new book
2. View all books
3. Log reading progress
4. View reading progress
5. Export book data
6. Import book data
7. Exit

Enter your choice (1-7): 4

Reading Progress:

Atomic Habits - 120/320 pages read (37.5%)
```
