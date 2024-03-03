class Book:

    def __init__(self):
        self.title = None
        self.year = None
        self.publisher = None
        self.genre = None
        self.author = None
        self.price = None

    def inputInfo(self):
        self.title = input('Введите название книги - ')
        self.year = input('Введите год выпуска книги - ')
        self.publisher = input('Введите издателя книги - ')
        self.genre = input('Введите жанр книги - ')
        self.author = input('Введите автора книги - ')
        self.price = input('Введите цену книги - ')

    def printInfoBook(self):
        print(f'Название книги {self.title}\n'
              f'Год выпуска книги {self.year}\n'
              f'Издатель книги {self.publisher}\n'
              f'Жанр книги {self.genre}\n'
              f'Автор книги {self.author}\n'
              f'Цена книги {self.price}')

    def tittleBook(self):
        return self.title

    def yearBook(self):
        return self.year

    def publisherBook(self):
        return self.publisher

    def genreBook(self):
        return self.genre

    def authorBook(self):
        return self.author

    def priceBook(self):
        return self.price


book = Book()

book.inputInfo()
book.printInfoBook()

title = book.tittleBook()

print(title)
