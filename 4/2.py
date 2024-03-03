number = int(input('Введите число: '))

degree = int(input('Введите степень от 0 - 7: '))

if 0 <= degree <= 7:
    print(number**degree)
else:
    print('Ввели неправильный диапазон')
