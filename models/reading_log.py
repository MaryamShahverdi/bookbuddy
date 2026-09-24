from datetime import datetime

class ReadingLog:
    def __init__(self, pages_read, notes="", date=None):
        self.pages_read = pages_read
        self.notes = notes
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "pages_read": self.pages_read,
            "notes": self.notes,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            pages_read=data["pages_read"],
            notes=data.get("notes", ""),
            date=data.get("date")
        )
