class Car:

    def __init__(self):
        self.model = None
        self.year = None
        self.factory = None
        self.engine = None
        self.color = None
        self.price = None

    def inputInfo(self):
        self.model = input('Введите модель автомобиля - ')
        self.year = input('Введите год выпуска автомобиля - ')
        self.factory = input('Введите производителя автомобиля - ')
        self.engine = input('Введите объем двигателя автомобиля - ')
        self.color = input('Введите цвет автомобиля - ')
        self.price = input('Введите цену автомобиля - ')

    def printInfoCar(self):
        print(f'Модель автомобиля {self.model}\n'
              f'Год выпуска автомобиля {self.year}\n'
              f'Производитель автомобиля {self.factory}\n'
              f'Объем двигателя автомобиля {self.engine}\n'
              f'Цвет автомобиля {self.color}\n'
              f'Цена автомобиля {self.price}')

    def modelInfo(self):
        return self.model

    def yearInfo(self):
        return self.year

    def factoryInfo(self):
        return self.factory

    def engineInfo(self):
        return self.engine

    def colorInfo(self):
        return self.color

    def priceInfo(self):
        return self.price

    def __call__(self, newModel, newYear, newFactory, newEngine, newColor, newPrice):
        self.model = newModel
        self.year = newYear
        self.factory = newFactory
        self.engine = newEngine
        self.color = newColor
        self.price = newPrice

carOne = Car()

carOne.inputInfo()
carOne.printInfoCar()

model = carOne.modelInfo()

print(model)

carTwo = Car()
carTwo('astra', '2012', 'opel', 1.5, 'red', 20000)
carTwo.printInfoCar()


