numOne = int(input("Введите количество метров: "))

result = int(input('Выберите единицу перевода: 1 - мили; 2 - дюймы; 3 - ярды '))

if result == 1:
    print(f'{numOne*0.000621371} - миль')
if result == 2:
    print(f'{numOne*39.3701} - дюймов')
if result == 3:
    print(f'{numOne*1.09361} - ярдов')

