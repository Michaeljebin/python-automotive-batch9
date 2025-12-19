class Library:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def borrow(self,books):
        if books in self.books:
            print(books, "book issued")
            self.books.remove(books)

    def return_book(self, book):
        self.books.append(book)
        print(book,"books added")

lib =Library ("1234","michael")
lib.books = ["One peice", "Naruto", "Bleach","Dragon ballz"]
lib.borrow("One peice")
lib.return_book("Demon slayer")

 

