from models.book import Book
from models.reading_log import ReadingLog
from exceptions.errors import BookNotFoundError, InvalidLogError
from utils.decorators import log_action

class ReadingTracker:
    def __init__(self):
        self.books = []

    @log_action
    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        return self.books

    def find_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        raise BookNotFoundError(f"Book '{title}' not found.")

    @log_action
    def log_reading(self, title, pages, notes=""):
        if pages <= 0:
            raise InvalidLogError("Pages must be positive.")
        book = self.find_book(title)
        book.add_log(ReadingLog(pages, notes))
