price = int(input('Введите стоимость разговора за 1 минуту: '))

operator = int(input('Выберете с кого на какой оператор вы звоните:\n'
                     '1 - с мегафона на билайн\n'
                     '2 - с мегафона на МТС\n'
                     '3 - с мегафона на МТС'))

result = 0

if (operator == 1):
    result = price * 1.2
    print(f'Стоимость = {result}')
elif (operator == 2):
    result = price * 1.05
    print(f'Стоимость = {result}')
elif (operator == 3):
    result = price * 1.5
    print(f'Стоимость = {result}')
else:
    print('error')
