from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection


class Test_Book:
    def test_init(self):
        b1 = Book()
        b2 = Book('Apple', 'James', 2005)
        assert b1.get_title() == ''
        assert b1.get_author() == ''
        assert b1.get_year() == None
        assert b2.get_title() == 'Apple'
        assert b2.get_author() == 'James'
        assert b2.get_year() == 2005

    def test_get_title(self):
        b1 = Book('Apple', 'James', 2005)
        assert b1.get_title() == 'Apple'

    def test_get_author(self):
        b1 = Book('Apple', 'James', 2005)
        assert b1.get_author() == 'James'

    def test_get_year(self):
        b1 = Book('Apple', 'James', 2005)
        assert b1.get_year() == 2005

    def test_get_book_details(self):
        b1 = Book('Apple', 'James', 2005)
        assert b1.get_book_details() == 'Title: Apple, Author: James, Year: 2005'

    def test_gt(self):
        b1 = Book('Apple', 'James', 2005)
        b2 = Book('Orange', 'Allen', 1990)
        assert b2 < b1
        b1 = Book('Apple', 'James', 2005)
        b2 = Book('Apple', 'James', 1995)
        assert b2 < b1
        b1 = Book('Apple', 'James', 2005)
        b2 = Book('Apple', 'James', 2005)
        assert not b1 > b2
        b1 = Book('Apple', 'James', 2005)
        b2 = Book('Banana', 'James', 2005)
        assert b2 > b1
        b1 = Book('Orange', 'Allen', 1990)
        b2 = Book('Peach', 'Smith', 1985)
        assert b1 > b2

class Test_BookCollection:
    def test_init(self):
        c = BookCollection()
        assert c.head == None

    def test_isempty(self):
        c = BookCollection()
        assert c.is_empty() is True
        c.head = BookCollectionNode(Book('Apple', 'James', 2005))
        assert c.is_empty() is False

    def test_get_number_of_books(self):
        c = BookCollection()
        assert c.get_number_of_books() == 0
        c.head = BookCollectionNode(Book('Apple', 'James', 2005))
        c.head.next = BookCollectionNode(Book('Orange', 'Allen', 1990))
        assert c.get_number_of_books() == 2

    def test_insert_book(self):
        c = BookCollection()
        b1 = Book('Apple', 'James', 2005)
        c.insert_book(b1)
        assert c.head.data == b1
        b2 = Book('Orange', 'Allen', 1990)
        c.insert_book(b2)
        assert c.head.data == b2
        assert c.head.next.data == b1
        b3 = Book('Banana', 'James', 2010)
        c.insert_book(b3)
        assert c.head.data == b2
        assert c.head.next.data == b1
        assert c.head.next.next.data == b3
        b4 = Book('Peach', 'Smith', 2005)
        c.insert_book(b4)
        assert c.head.data == b2
        assert c.head.next.data == b1
        assert c.head.next.next.data == b3
        assert c.head.next.next.next.data == b4

    def test_get_books_by_author(self):
        c = BookCollection()
        c.head = BookCollectionNode(Book('Apple', 'James', 2005))
        c.head.next = BookCollectionNode(Book('Orange', 'James', 1990))
        assert c.get_books_by_author('Allen') == ''
        assert c.get_books_by_author('James') == 'Title: Apple, Author: James, Year: 2005\nTitle: Orange, Author: James, Year: 1990\n'

    def test_get_all_books_in_collection(self):
        c = BookCollection()
        assert c.get_all_books_in_collection() == ''
        c.head = BookCollectionNode(Book('Apple', 'James', 2005))
        c.head.next = BookCollectionNode(Book('Orange', 'Allen', 1990))
        assert c.get_all_books_in_collection() == 'Title: Apple, Author: James, Year: 2005\nTitle: Orange, Author: Allen, Year: 1990\n'

    def test_remove_author(self):
        c = BookCollection()
        c.head = BookCollectionNode(Book("Apples", "Allen", 2000))
        c.head.next = BookCollectionNode(Book("Oranges", "Allen", 2005))
        c.head.next.next = BookCollectionNode(Book("Banana", "James", 2010))
        c.remove_author("Allen")
        assert c.get_all_books_in_collection() == "Title: Banana, Author: James, Year: 2010\n"
        c = BookCollection()
        c.head = BookCollectionNode(Book("Apples", "Allen", 2000))
        c.head.next = BookCollectionNode(Book("Oranges", "Allen", 2005))
        c.head.next.next = BookCollectionNode(Book("Banana", "James", 2010))
        c.remove_author("James")
        assert c.get_all_books_in_collection() == "Title: Apples, Author: Allen, Year: 2000\nTitle: Oranges, Author: Allen, Year: 2005\n"

    def test_recursive_search_title(self):
        c = BookCollection()
        c.head = BookCollectionNode(Book('Apple', 'James', 2005))
        c.head.next = BookCollectionNode(Book('Orange', 'Allen', 1990))
        assert c.recursive_search_title('Orange', c.head) is True
        assert c.recursive_search_title('Banana', c.head) is False

class TestBookCollectionNode:
    def test_init(self):
        node = BookCollectionNode()
        assert node.data is None
        assert node.next is None

    def test_get_data(self):
        book = Book('Apple', 'James', 2005)
        node = BookCollectionNode(book)
        assert node.get_data() == book

    def test_get_next(self):
        book = Book('Orange', 'Allen', 2005)
        node = BookCollectionNode(book)
        assert node.get_next() is None
        next_book = Book('Apple', 'James', 1990)
        next_node = BookCollectionNode(next_book)
        node.set_next(next_node)
        assert node.get_next() == next_node

    def test_set_data(self):
        node = BookCollectionNode()
        book = Book('Orange', 'Allen', 2005)
        node.set_data(book)
        assert node.get_data() == book

    def test_set_next(self):
        b1 = Book('Orange', 'Allen', 2005)
        bn1 = BookCollectionNode(b1)
        b2 = Book('Apple', 'James', 1990)
        bn2 = BookCollectionNode(b2)
        bn1.set_next(bn2)
        assert bn1.get_next() == bn2
