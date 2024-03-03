numOne = int(input("Введите первое число: "))
numTwo = int(input("Введите второе число: "))
numThree = int(input("Введите третье число: "))

result = int(input("Выберите действие: 1 - максимальное число; 2 - Минимальное число; "
                   "3 - среднеарифметическое трёх чисел"))

if result == 1:
    if numOne > numTwo and numOne > numThree:
        print(f'Максимальное число = {numOne}')
    if numTwo > numOne and numTwo > numThree:
        print(f'Максимальное число = {numTwo}')
    if numThree > numOne and numThree > numTwo:
        print(f'Максимальное число = {numThree}')
elif result == 2:
    if numOne < numTwo and numOne < numThree:
        print(f'Минимальное число число = {numOne}')
    if numTwo < numOne and numTwo < numThree:
        print(f'Минимальное число = {numTwo}')
    if numThree > numOne and numThree < numTwo:
        print(f'Минимальное число = {numThree}')
elif result == 3:
    print(f'Cреднеарифметическое число - {(numOne+numTwo+numThree)/3}')
