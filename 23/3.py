class Stadium:

    def __init__(self):
        self.name = None
        self.openingDate = None
        self.country = None
        self.city = None
        self.capacity = None

    def inputInfo(self):
        self.name = input('Введите название стадиона - ')
        self.openingDate = input('Введите дату открытия стадиона - ')
        self.country = input('Введите страну стадиона - ')
        self.city = input('Введите город стадиона - ')
        self.capacity = input('Введите вместимость стадиона - ')

    def printInfoStadium(self):
        print(f'Название стадионв {self.name}\n'
              f'Дата открытия стадиона {self.openingDate}\n'
              f'Страна стадиона {self.country}\n'
              f'Город стадиона {self.city}\n'
              f'Вместимость стадиона {self.capacity}')

    def nameStadium(self):
        return self.name

    def openingDateStadium(self):
        return self.openingDate

    def countryStadium(self):
        return self.country

    def cityStadium(self):
        return self.city

    def capacityStadium(self):
        return self.capacity


stadium = Stadium()

stadium.inputInfo()
stadium.printInfoStadium()

name = stadium.nameStadium()

print(name)
