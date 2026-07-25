class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

b1 = Book("Python Programming", "John")
b1.display()