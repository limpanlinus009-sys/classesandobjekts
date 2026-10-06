
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


book1 = Book("Biblen", "J.K. Jesus", 2358)
book2 = Book("Harry Potter", "J.K. Rowling", 500)

book1.show_info()
print()
book2.show_info()

