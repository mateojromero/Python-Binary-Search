
from Book import Book

class BookCollectionNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newData=None):
        self.data = newData

    def set_next(self, newNext=None):
        self.next = newNext
