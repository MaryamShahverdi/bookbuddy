from models.book import Book

class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size_mb, date_added=None):
        super().__init__(title, author, genre, pages, date_added)
        self.file_size_mb = file_size_mb
