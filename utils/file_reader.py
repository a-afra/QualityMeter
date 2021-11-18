import os
from antlr4 import *


class FileReader:
    def __init__(self):
        pass

    @classmethod
    def getFileStream(cls, file):
        return FileStream(file, encoding='utf-8')

    @classmethod
    def getFileStreams(cls, path):
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file() and entry.name.endswith('.java'):
                    yield cls.getFileStream(entry.path)
                elif entry.is_dir():
                    yield from cls.getFileStreams(entry.path)
