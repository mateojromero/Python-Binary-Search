class Book:
    def __init__(self, title='', author='', year=None):
        self.title = title
        self.author = author
        self. year = year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_book_details(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
    
    def __gt__(self, other):
        if self.author > other.author:
            return True
        elif self.author == other.author:
            if self.year > other.year:
                return True
            elif self.year == other.year:
                return self.title > other.title
        return False
