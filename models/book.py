from models.reading_log import ReadingLog

class Book:
    def __init__(self, title, author, genre, pages, date_added=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.date_added = date_added
        self.__pages_read = 0
        self.reading_logs = []

    @property
    def pages_read(self):
        return self.__pages_read

    @property
    def progress(self):
        return (self.__pages_read / self.pages) * 100 if self.pages > 0 else 0

    def add_log(self, log: ReadingLog):
        self.reading_logs.append(log)
        self.__pages_read = min(self.pages, self.__pages_read + log.pages_read)

    def to_dict(self):
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages,
            "date_added": self.date_added,
            "pages_read": self.__pages_read,
            "reading_logs": [log.to_dict() for log in self.reading_logs]
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            pages=data["pages"],
            date_added=data.get("date_added")
        )
        obj._Book__pages_read = data.get("pages_read", 0)
        obj.reading_logs = [
            ReadingLog.from_dict(d) for d in data.get("reading_logs", [])
        ]
        return obj

    def __str__(self):
        return f"{self.title} by {self.author} [{self.genre}] - {self.pages} pages"
