import os


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, "w+")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            return True


with File('file_1.txt', 'r') as f:
    date = f.write('Hello')
