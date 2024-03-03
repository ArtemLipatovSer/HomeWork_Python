class Ship:
    def __init__(self, model, country, year):
        self.model = model
        self.country = country
        self. year = year

class Frigate(Ship):
    def __init__(self, model, country, year, classShip):
        super().__init__(model, country, year)
        self.classShip = classShip

    def __str__(self):
        return f'Модель корабля - {self.model}, страна изготовителя - {self.country}, год выпуска - {self.year}, ' \
               f'класс корабля - {self.classShip}'

class Destroyer(Ship):
    def __init__(self, model, country, year, displacement):
        super().__init__(model, country, year)
        self.displacement = displacement

    def __str__(self):
        return f'Модель корабля - {self.model}, страна изготовителя - {self.country}, год выпуска - {self.year}, ' \
               f'водоизмещение корабля - {self.displacement}'


class Cruiser(Ship):
    def __init__(self, model, country, year, weightType):
        super().__init__(model, country, year)
        self.weightType = weightType

    def __str__(self):
        return f'Модель корабля - {self.model}, страна изготовителя - {self.country}, год выпуска - {self.year}, ' \
               f'подкласс по массе - {self.weightType}'


obj1 = Frigate('Фрегат', 'CCCР', 1991, 'военный')
obj2 = Destroyer('Эсминец', 'CCCР', 1991, '3000 тон')
obj3 = Cruiser('Крейсер', 'CCCР', 1991, 'тяжелый')

print(obj1)
print(obj2)
print(obj3)
