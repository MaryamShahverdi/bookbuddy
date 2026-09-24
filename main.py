import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.reading_tracker import ReadingTracker
from storage.data_exporter import DataExporter
from exceptions.errors import BookNotFoundError, InvalidLogError, StorageError
from models.book import Book

def show_menu():
    print("\nWelcome to BookBuddy!")
    print("Track your reading, log progress, and manage your personal library.\n")
    print("Main Menu:")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Log reading progress")
    print("4. View reading progress")
    print("5. Export book data")
    print("6. Import book data")
    print("7. Exit\n")

def pause():
    print("Returning to main menu...\n")

def add_book_cli(tracker):
    print("\nAdd a New Book\n")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    try:
        pages = int(input("Enter total pages: "))
    except ValueError:
        print("\nInvalid input.")
        return

    book = Book(title, author, genre, pages)
    tracker.add_book(book)
    print(f"\nBook '{title}' added successfully!")
    pause()

def library_cli(tracker):
    print("\nYour Library:\n")
    books = tracker.list_books()
    if not books:
        print("No books available.\n")
        pause()
        return
    for i, b in enumerate(books, start=1):
        print(f"{i}. {b}")
    print()
    pause()

def log_reading_cli(tracker):
    print("\nLog Reading Progress\n")
    title = input("Enter book title: ")
    try:
        pages = int(input("Enter pages read: "))
    except ValueError:
        print("\nInvalid input.")
        return
    notes = input("Enter notes : ")
    try:
        tracker.log_reading(title, pages, notes)
        print("\nReading log added!")
    except BookNotFoundError :
        pass
    pause()

def view_progress_cli(tracker):
    print("\nReading Progress:\n")
    books = tracker.list_books()
    if not books:
        print("No books available.\n")
        pause()
        return
    for b in books:
        print(f"{b.title} - {b.pages_read}/{b.pages} pages read ({b.progress:.1f}%)")
    print()
    pause()

def export_data_cli(tracker):
    print("\nExport Book Data\n")
    filename = input("Enter filename : ")
    try:
        DataExporter.export(filename, tracker.books)
        print(f"\nData exported to '{filename}'")
    except StorageError :
        pass
    pause()

def import_data_cli(tracker):
    print("\nImport Book Data\n")
    filename = input("Enter filename: ")
    try:
        tracker.books = DataExporter.load(filename)
        print("\nBooks imported successfully!")
    except StorageError:
        pass
    pause()

def main():
    tracker = ReadingTracker()
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()
        try:
            if choice == "1": add_book_cli(tracker)
            elif choice == "2": library_cli(tracker)
            elif choice == "3": log_reading_cli(tracker)
            elif choice == "4": view_progress_cli(tracker)
            elif choice == "5": export_data_cli(tracker)
            elif choice == "6": import_data_cli(tracker)
            elif choice == "7": break
            else: print("Invalid choice.try again.\n")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            pause()

if __name__ == "__main__":
    main()
