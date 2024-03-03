maxNum = -1000000
minNum = 1000000
sumNum = 0

while True:
    number = int(input('Введите число: '))
    if number == 7:
        print('Good bye!')
        break
    sumNum += number
    print(f'Сумма введеных чисел - {sumNum}')
    if number > maxNum:
        maxNum = number
    print(f'Максимальное введенное число - {maxNum}')
    if number < minNum:
        minNum = number
    print(f'Минимальное введенное число - {minNum}')
