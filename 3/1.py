numOne = int(input("Введите первое число: "))
numTwo = int(input("Введите второе число: "))
numThree = int(input("Введите третье число: "))

result = int(input("Выберите действие: 1 - сложить; 2 - умножить"))

if result == 1:
    print(f'Сумма чисел = {numOne+numTwo+numThree}')
elif result == 2:
    print(f'Произведение чисел = {numOne*numTwo*numThree}')
else:
    print('Такого выбора нет')
