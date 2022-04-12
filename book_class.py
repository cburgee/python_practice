class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.pages = pages
        self.copies = copies

    def display(self):
        print(
            self.isbn,
            self.title,
            self._price,
            self.copies,
        )

    def in_stock(self):
        if self.copies:
            return True
        else:
            return False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print("This book is currently out of stock.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 50 and new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError("Sorry, the price is too low!")


book_1 = Book("957-4-36-547417-1", "Learn Physics", "Stephen", "CBC", 350, 200, 10)
book_2 = Book("652-6-86-748413-3", "Learn Chemistry", "Jack", "CBC", 400, 220, 20)
book_3 = Book("957-7-39-347216-2", "Learn Math", "John", "XYZ", 500, 300, 5)
book_4 = Book("957-7-39-347216-2", "Learn Biology", "Jack", "XYZ", 400, 200, 6)
book_list = [book_1, book_2, book_3, book_4]
jack_book_list = []


def display_each(book_list):
    for b in book_list:
        b.display()


def get_author_jack(book_list, new_list):
    for b in book_list:
        if b.author == "Jack":
            new_list.append(b)
    return new_list


def main():
    book_1.sell()
    book_2.sell()
    display_each(get_author_jack(book_list, jack_book_list))


main()
