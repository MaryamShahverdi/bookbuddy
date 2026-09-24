import json
from utils.retry import retry_operation
from utils.context import SafeFileManager
from exceptions.errors import StorageError
from models.book import Book

class JSONHandler:
    @staticmethod
    @retry_operation()
    def save(filename, books):
        try:
            with SafeFileManager(filename, "w") as f:
                json.dump([b.to_dict() for b in books], f, indent=4)
        except Exception as e:
            raise StorageError(str(e))

    @staticmethod
    @retry_operation()
    def load(filename):
        try:
            with SafeFileManager(filename, "r") as f:
                data = json.load(f)
            return [Book.from_dict(d) for d in data]
        except FileNotFoundError:
            return []
        except Exception as e:
            raise StorageError(str(e))
