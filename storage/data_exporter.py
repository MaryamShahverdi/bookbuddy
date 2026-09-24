from storage.json_handler import JSONHandler

class DataExporter:
    @staticmethod
    def export(filename, books):
        JSONHandler.save(filename, books)

    @staticmethod
    def load(filename):
        return JSONHandler.load(filename)
