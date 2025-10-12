# library_system.py

class Book:
    """Base class representing a general book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition — manages a collection of books."""
    def __init__(self):
        self.books = []  # holds instances of Book, EBook, and PrintBook

    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added to the library.")

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)

