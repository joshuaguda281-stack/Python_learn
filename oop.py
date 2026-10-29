# oop = object-oriented programing


# properties + functions
# class # template

# book title, auther, isbn, price
class Book:
    def __init__(self, title, author, year, isbn, price):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.price = price

    def print_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("ISBN:", self.isbn)
        print("Price:", self.price)
        print("----------------")

    def apply_discount(self, discount):
        self.price *= 1 - discount / 100
        print("New price:", self.price)



b1 = Book(title="Two rivers", author="", year=1999, isbn=9, price=2000)
b2 = Book(title="TBT", author="", year=2001, isbn=9, price=2000)
b1.print_details()
b2.print_details()
