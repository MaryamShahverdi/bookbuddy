from models.book import Book

class AudioBook(Book):
    def __init__(self, title, author, genre, pages, duration_minutes, date_added=None):
        super().__init__(title, author, genre, pages, date_added)
        self.duration_minutes = duration_minutes
