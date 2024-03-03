class Temp:
    count = 0
    @staticmethod
    def cels(temp):
        Temp.count += 1
        return f'{((temp - 32) * (5 / 9))} градусов'

    @staticmethod
    def faren(temp):
        Temp.count += 1
        return f'{((temp * (9 / 5)) +32)} градусов Фаренгейта'

    @staticmethod
    def result():
        return f'Количество подсчетов температуры - {Temp.count}'

print(Temp.cels(55))
print(Temp.faren(55))
print(Temp.faren(80))
print(Temp.faren(55))

print(Temp.result())
