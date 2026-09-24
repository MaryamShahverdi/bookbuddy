class BookBuddyError(Exception):
    pass

class BookNotFoundError(BookBuddyError):
    pass

class InvalidLogError(BookBuddyError):
    pass

class StorageError(BookBuddyError):
    pass
