class Device:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year


class CoffeeMachine(Device):
    def __init__(self, brand, year, name, coffeeUsed):
        super().__init__(brand, year, name)
        self.coffeUsed = coffeeUsed

    def __str__(self):
        return f'Приспособление - {self.name}, изготовитель - {self.brand}, год выпуска - {self.year}, ' \
               f'используемый кофе - {self.coffeUsed}'


class Blender(Device):
    def __init__(self, brand, year, name, typeBlender):
        super().__init__(brand, year, name)
        self.typeBlender = typeBlender

    def __str__(self):
        return f'Приспособление - {self.name}, изготовитель - {self.brand}, год выпуска - {self.year}, ' \
               f'тип блендера - {self.typeBlender}'


class MeatGrinder(Device):
    def __init__(self, brand, year, name, typeMeatGrinder):
        super().__init__(brand, year, name)
        self.typeMeatGrinder = typeMeatGrinder

    def __str__(self):
        return f'Приспособление - {self.name}, изготовитель - {self.brand}, год выпуска - {self.year}, ' \
               f'тип привода - {self.typeMeatGrinder}'


obj1 = CoffeeMachine('кофе машина', 'bosch', 2023, 'молотый')
obj2 = Blender('блендер', 'bosch', 2023, 'погружной')
obj3 = MeatGrinder('мясорубка', 'bosch', 2023, 'электрический')

print(obj1)
print(obj2)
print(obj3)
