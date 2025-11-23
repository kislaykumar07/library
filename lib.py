class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def _str_(self):
        status = "Available" if self.available else "Not available"
        return f"{self.title} written by {self.author}"
class Library:
    def _init_(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to the library")
    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You have borrowed {book.title}")
            else:
                print(f"{book.title} currently not available")
            return
        print("Book not found in this library")
    def return_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"{book.title} returned")
            else:
                print(f"{book.title} was not borrowed")
                return
            print("Book was not borrowed from this library")
    def display_books(self):
        print("List of Books")
        if not self.books:
            print("No book added in this library yet")
        else:
            for book in self.books:
                print(book)

def run_library():
    library = Library()

    while True:
        print("Welcome to kislay's library")
        print("1-> Display book")
        print("2-> Add  book")
        print("3-> Borrow book")
        print("4-> Return book")
        print("5-> Quit")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Enter a valid number")
        if choice == 2:
            title = input("Enter the Title of your book: ")
            author = input("Enter the author of yout book: ")
            library.add_book(Book(title, author))
        elif choice == 1:
            library.display_books()
        elif choice == 3:
            title = input("Enter the Title of your book: ")
            library.lend_book(title)
        elif choice == 4:
            title = input("Enter the Title of your book: ")
            library.return_book(title)
        elif choice == 5:
            print("Thanks for visiting :))")
            break
        else:
            print("Enter a number in range(1-5)!!")
run_library()