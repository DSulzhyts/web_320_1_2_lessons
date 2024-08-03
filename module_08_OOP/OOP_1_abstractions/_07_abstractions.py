# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#
# book = Book("Дубровский", "А.С. Пушкин")
# print(book.title)
# print(book.author)
#
# book.title = "Капитанская дочка"
# book.author = "Пушкин А.С."
# print(book.title)
# print(book.author)


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author


book = Book("Дубровский", "А.С. Пушкин")
print(book.get_title())
print(book.get_author())
book.__title = "Капитанская дочка"
book.__author = 'Пушкин A.C.'
print(book.get_title())
print(book.get_author())

