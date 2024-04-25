
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def get_number_of_books(self):
        cur = self.head
        total = 0
        while cur is not None:
            cur = cur.next
            total += 1
        return total

    def insert_book(self, book):
        new_node = BookCollectionNode(book)
        if self.head is None or book < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < book:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def get_books_by_author(self, author):
        books = ''
        cur = self.head
        while cur:
            if cur.data.get_author().lower() == author.lower():
                books += cur.data.get_book_details() + '\n'
            cur = cur.next
        return books

    def get_all_books_in_collection(self):
        book_details = ''
        cur = self.head
        while cur:
            book_details += cur.data.get_book_details() + "\n"
            cur = cur.next
        return book_details

    def remove_author(self, author):
        cur = self.head
        prev = None
        while cur:
            if cur.data.get_author().lower() == author.lower():
                if prev:
                    prev.next = cur.next
                else:
                 self.head = cur.next
            else:
                prev = cur
            cur = cur.next


    def recursive_search_title(self, title, bookNode):
        if bookNode is None:
            return False
        elif bookNode.data.get_title().lower() == title.lower():
            return True
        else:
            return self.recursive_search_title(title, bookNode.next)
