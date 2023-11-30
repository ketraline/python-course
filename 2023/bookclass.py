class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def print_book(self):
        print(f"{self.title} by {self.author}, {self.year}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("added", book.title, "by", book.author)
    
    def display_books(self):
        for book in self.books:
            if book.is_available:
                book.print_book()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                print("borrowing ", book.title, " by ", book.author)
                book.is_available = False
                return
        print("book is not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available == False:
                print("returning ", book.title, " by ", book.author)
                book.is_available = True
                return
        print("book is in the library")

book1 = Book("Bible", "God", 0)
book2 = Book("Meow", "Cat", 2019)
book3 = Book("Meow 2", "Cat 2", 2020)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()
x = input("what book would you like to borrow? (title) ")
library.borrow_book(x)
library.borrow_book(x)
x = input("what book would you like to return? (title) ")
library.return_book("Bible")
